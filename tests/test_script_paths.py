import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ScriptLocationTests(unittest.TestCase):
    def run_script_from_other_directory(
        self, script_name, fixture_names, expected_outputs
    ):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            project_dir = temporary_root / "project"
            working_dir = temporary_root / "elsewhere"
            project_dir.mkdir()
            working_dir.mkdir()

            for filename in (script_name, *fixture_names):
                shutil.copy2(REPO_ROOT / filename, project_dir / filename)

            environment = os.environ.copy()
            environment["MPLBACKEND"] = "Agg"
            result = subprocess.run(
                [sys.executable, str(project_dir / script_name)],
                cwd=working_dir,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            for filename in expected_outputs:
                self.assertTrue((project_dir / filename).is_file(), filename)
                self.assertFalse((working_dir / filename).exists(), filename)
            return result.stdout

    def test_cleaning_script_uses_files_next_to_itself(self):
        stdout = self.run_script_from_other_directory(
            "pandascodefile.py",
            ("Titanic-Dataset.csv",),
            ("cleaned_titanic.csv",),
        )

        self.assertIn("After cleaning: (891, 12)", stdout)

    def test_analysis_script_reads_and_writes_next_to_itself(self):
        stdout = self.run_script_from_other_directory(
            "analysis.py",
            ("cleaned_titanic.csv",),
            (
                "survival_by_gender.png",
                "survival_by_class.png",
                "age_distribution.png",
            ),
        )

        self.assertIn("Charts saved:", stdout)


if __name__ == "__main__":
    unittest.main()
