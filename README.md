# SOFAR_nav01

The husky robot is able to reach the target

## Packages
to execute the launch files it is necessary to install some packages.
```bash
sudo apt-get install ros-noetic-openslam-gmapping
sudo apt-get install ros-noetic-navigation
sudo apt-get install ros-noetic-lms1xx
```

## Notes
Some parameters have been changed in order for the costmap to be updated in time and be sufficently wide so the robot doesn't drive too close to the walls.
Moreover, the parameter of the topic "scan" in the costmap_common_params.yaml file has been changed to "laser_scan".
The map is decently build when the fixed frame in rviz is "map", so be sure to set that. Withi this setting you'll get an error on the laser object but it works anyways.
The behaviour may be different for you epending on the setup that you are using. I'm using Unity on native windows and ROS on a Ubunty VM, so it is not particularly reactive. The quality might improve with a two computers setup.
