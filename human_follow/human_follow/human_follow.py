import rclpy
from rclpy.node import Node
from your_package_name.msg import ObjectInformation 

class ObjectInformationSubscriber(Node):
    def __init__(self):
        super().__init__('object_information_subscriber')
        self.subscription = self.create_subscription(
            ObjectInformation, '/human_detector/object_informations',
            self.callback, 10)
        self.subscription  # keep reference to subscription object
        self.get_logger().info('Subscribed to /human_detector/object_informations topic')

    def callback(self, msg):
        # 특정 조건에 맞는 데이터만 가져오기
        if msg.camera_id == 0 and msg.index == 0.0:
            # 받은 메시지에서 필요한 데이터 처리
            self.get_logger().info(f"Received data: Camera ID - {msg.camera_id}, Index - {msg.index}")
            self.get_logger().info(f"Label - {msg.label}, Distance - {msg.distance}")
            # 원하는 작업 수행

def main(args=None):
    rclpy.init(args=args)
    object_information_subscriber = ObjectInformationSubscriber()
    rclpy.spin(object_information_subscriber)
    object_information_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()