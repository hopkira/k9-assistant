import picamera
import numpy
import io

from edgetpu.detection.engine import DetectionEngine
from edgetpu.utils import dataset_utils

engine = DetectionEngine('/home/pi/k9-assistant/model.tflite')

def main():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        _, height, width, _ = engine.get_input_tensor_shape()
        camera.start_preview()
        try:
            stream = io.BytesIO()
            for _ in camera.capture_continuous(
                stream, format='rgb', use_video_port=True, resize=(width, height)):
                stream.truncate()
                stream.seek(0)
                input_tensor = np.frombuffer(stream.getvalue(), dtype=np.uint8)
                start_ms = time.time()
                results = engine.classify_with_input_tensor(input_tensor, top_k=1)
                elapsed_ms = time.time() - start_ms
                if results:
                camera.annotate_text = '%s %.2f\n%.2fms' % (
                    labels[results[0][0]], results[0][1], elapsed_ms * 1000.0)
        finally:
        camera.stop_preview()


if __name__ == '__main__':
  main()