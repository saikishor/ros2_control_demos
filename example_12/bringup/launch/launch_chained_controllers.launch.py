# Copyright 2021 Stogl Robotics Consulting UG (haftungsbeschränkt)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from launch import LaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch_ros.actions import Node
from controller_manager.launch_utils import generate_load_controller_launch_description

import os

from ament_index_python.packages import get_package_share_directory



def generate_launch_description():

  return generate_load_controller_launch_description(
          controller_name='test_position_controller',
          controller_type='passthrough_controller/PassthroughController',
          controller_params_file=os.path.join(
              get_package_share_directory('ros2_control_demo_example_12'),
              'config', 'rrbot_chained_controllers.yaml')
      )

