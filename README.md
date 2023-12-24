## Installation

1. Install `async-web-server-cpp` for ROS Noetic:
   ```bash
   sudo apt install ros-noetic-async-web-server-cpp
   ```

2. Install `rosbridge-server` for ROS Noetic:
   ```bash
   sudo apt-get install ros-noetic-rosbridge-server
   ```

3. Clone the `web_video_server` repository:
   ```bash
   cd ~/catkin_ws/src
   git clone https://github.com/RobotWebTools/web_video_server.git
   ```

4. For running in simulation, clone the robot model:
   ```bash
   git clone https://github.com/AkshayaJeyaprakash/my_robot.git
   ```

## Running Sequence

1. Start ROS core:
   ```bash
   roscore
   ```

2. Run the robot subscriber (replace `[run the robot subscriber]` with actual command).

3. Start the web video server (to stream robot camera):
   ```bash
   rosrun web_video_server web_video_server
   ```
   Access the stream at: [http://localhost:8080/stream?topic=/robot_camera/camera/image_raw](http://localhost:8080/stream?topic=/robot_camera/camera/image_raw)

4. For simulation, launch the robot simulation:
   ```bash
   roslaunch my_robot robot_simulation.launch
   ```
   (No need run on a physical robot)

5. Launch the ROSBridge WebSocket server:
   ```bash
   roslaunch rosbridge_server rosbridge_websocket.launch
   ```
   WebSocket address: [ws://0.0.0.0:9090](ws://0.0.0.0:9090)

6. Run the Python app for web interface:
   ```bash
   python app.py
   ```
   Access the web interface at: [http://localhost:5000](http://localhost:5000)

7. Monitor keyboard inputs sent to the robot:
   ```bash
   rostopic echo /my_robot/keyboard_input
   ```
