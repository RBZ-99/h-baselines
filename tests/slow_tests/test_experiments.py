"""Contains tests for the model abstractions and different models."""
import unittest
import os
import shutil
import ray

from hbaselines.utils.train import parse_options
from experiments.run_fcnet import main as run_fcnet
from experiments.run_hrl import main as run_hrl
from experiments.run_multi_fcnet import main as run_multi_fcnet


class TestExperimentRunnerScripts(unittest.TestCase):
    """Tests the runner scripts in the experiments folder."""

    def test_run_fcent_td3(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
        ])
        run_fcnet(args, 'data/fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(os.getcwd(), "data/fcnet/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_fcent_sac(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "SAC"
        ])
        run_fcnet(args, 'data/fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(os.getcwd(), "data/fcnet/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_fcent_failure(self):
        # Run the script; verify it fails.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "woops"
        ])
        self.assertRaises(ValueError, run_fcnet,
                          args=args, base_dir='data/fcnet')

        # Clear anything that was generated.
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_hrl_td3(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--initial_exploration_steps", "1",
            "--batch_size", "32",
            "--meta_period", "5",
            "--total_steps", "500",
            "--log_interval", "500",
        ])
        run_hrl(args, 'data/goal-conditioned')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/goal-conditioned/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_hrl_sac(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--initial_exploration_steps", "1",
            "--batch_size", "32",
            "--meta_period", "5",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "SAC"
        ])
        run_hrl(args, 'data/goal-conditioned')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/goal-conditioned/MountainCarContinuous-v0")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_hrl_failure(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--initial_exploration_steps", "1",
            "--batch_size", "32",
            "--meta_period", "5",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "woops"
        ])

        self.assertRaises(ValueError, run_hrl,
                          args=args, base_dir='data/goal-conditioned')

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_td3_independent(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_sac_independent(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "SAC"
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_failure_independent(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "woops"
        ])

        self.assertRaises(ValueError, run_multi_fcnet,
                          args=args, base_dir='data/multi-fcnet')

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_td3_shared(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--shared",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_sac_shared(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--shared",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "SAC"
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_failure_shared(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--shared",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "woops"
        ])

        self.assertRaises(ValueError, run_multi_fcnet,
                          args=args, base_dir='data/multi-fcnet')

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_td3_maddpg_independent(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--maddpg",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_sac_maddpg_independent(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--maddpg",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "SAC"
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_failure_maddpg_independent(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--maddpg",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "woops"
        ])

        self.assertRaises(ValueError, run_multi_fcnet,
                          args=args, base_dir='data/multi-fcnet')

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_td3_maddpg_shared(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--shared",
            "--maddpg",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_sac_maddpg_shared(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "multiagent-ring_small",
            "--shared",
            "--maddpg",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "SAC"
        ])
        run_multi_fcnet(args, 'data/multi-fcnet')

        # Check that the folders were generated.
        self.assertTrue(os.path.isdir(
            os.path.join(
                os.getcwd(),
                "data/multi-fcnet/multiagent-ring_small")))

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))

    def test_run_multi_fcnet_failure_maddpg_shared(self):
        # Run the script; verify it executes without failure.
        args = parse_options('', '', args=[
            "MountainCarContinuous-v0",
            "--shared",
            "--maddpg",
            "--initial_exploration_steps", "1",
            "--total_steps", "500",
            "--log_interval", "500",
            "--alg", "woops"
        ])

        self.assertRaises(ValueError, run_multi_fcnet,
                          args=args, base_dir='data/multi-fcnet')

        # Clear anything that was generated.
        ray.shutdown()
        shutil.rmtree(os.path.join(os.getcwd(), "data"))


if __name__ == '__main__':
    unittest.main()
