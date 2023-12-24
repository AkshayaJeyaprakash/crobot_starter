var ros = new ROSLIB.Ros({url : 'ws://localhost:9090'});
var linear_speed = 0;
var angular_speed = 0;
var speed_increase_percentage = 5;


var topic = new ROSLIB.Topic({
      ros : ros,
      name : '/my_robot/keyboard_input',
      messageType : 'std_msgs/String'
    })


function goForward(){
    console.log("forward")
    message = new ROSLIB.Message("up");
    topic.publish(message);
}

function goBack(){
    message = new ROSLIB.Message("down");
    topic.publish(this.message);
  }

function goRight(){
    console.log("r")
    message = new ROSLIB.Message("right");
    topic.publish(this.message);
}

function goLeft(){
    console.log("l")
    message = new ROSLIB.Message("left");
    topic.publish(this.message);
}

function Stop(){
    linear_speed = 0
    angular_speed = 0
}
