#!/usr/bin/python

from DS4Controller.src import controller
from time import sleep
from multiprocessing import Queue


def main(out_arduino_wheel_speed_queue, out_run_prog_queue):
    # init ds4 controller
    ds4_controller = controller.newController()

    # lets us know when to exit to program
    square_pressed = False
    reverse = False

    # Speed of the wheels
    prev_left = 0.0
    prev_right = 0.0
    while ds4_controller.active and square_pressed is False:

        if controller.getButtonDown(controller.BTN_SQUARE):
            reverse = not reverse
            print "Reverse: " + str(reverse)

        try:
            if controller.getAxisDown(controller.AXIS_R2):
                right_wheels = float(
                    controller.getAxisValue(controller.AXIS_R2))
                print right_wheels
            else:
                right_wheels = 0.0
            if controller.getAxisDown(controller.AXIS_L2):
                left_wheels = float(
                    controller.getAxisValue(controller.AXIS_L2))
                print left_wheels
            else:
                left_wheels = 0.0

            if reverse is True:
                left_wheels = float(-left_wheels)
                right_wheels = float(-right_wheels)

        except ValueError:
            left_wheels = "0"
            right_wheels = "0"

        if right_wheels != prev_right or left_wheels != prev_left:
            out_arduino_wheel_speed_queue.put((float(left_wheels),
                                               float(right_wheels)))

        prev_left = float(left_wheels)
        prev_right = float(right_wheels)

        if controller.getButtonDown(controller.BTN_CIRCLE):
            square_pressed = True
            out_run_prog_queue.put(False)

        sleep(.1)


if __name__ == '__main__':
    test_arduino_queue = Queue()
    test_running_program_queue = Queue()
    main(test_arduino_queue, test_running_program_queue)
