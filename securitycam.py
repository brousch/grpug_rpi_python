import picamera

if __name__ == "__main__":
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.framerate = 30
        camera.start_preview()
        camera.start_recording('securitycam/highres.h264')
        camera.start_recording('securitycam/lowres.h264',
                               splitter_port=2,
                               resize=(160, 90)) 
        camera.capture('securitycam/ss-00.jpg', use_video_port=True)
        camera.wait_recording(5)
        camera.capture('securitycam/ss-05.jpg', use_video_port=True)
        camera.wait_recording(5)
        camera.capture('securitycam/ss-10.jpg', use_video_port=True)
        camera.stop_recording(splitter_port=2)
        camera.stop_recording()
        camera.stop_preview()
