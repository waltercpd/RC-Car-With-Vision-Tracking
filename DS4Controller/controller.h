#include <fcntl.h>
#include <stdio.h>
#include <linux/types.h>
#include <errno.h>
#include <stdlib.h>

#define JOYSTICK_DEVICE  "/dev/input/js0"
#define JOYSTICK_DEVICE1  "/dev/input/js1"

#define JS_EVENT_BUTTON         0x01     /* button pressed/released */
#define JS_EVENT_AXIS           0x02     /* joystick moved */
#define JS_EVENT_INIT           0x80     /* initial state of device */
#define NUMBER_OF_BUTTONS       0x12     /* number of buttons on the ps4 controller */

struct  JoystickEvent {
  __u32 time;     /* eveimestamp in milliseconds */
  __s16 value;    /* value */
  __u8 type;      /* event type */
  __u8 number;    /* axis/button number */
};

struct JoystickInput {
  int button[NUMBER_OF_BUTTONS];
  int axis[NUMBER_OF_BUTTONS];
};

//
extern void Init_DS4(const char *command);

// Opens the joystick device file
extern int OpenJoystick();

//
extern int GetJoystickStatus(struct JoystickInput *wjse);

//
extern int GetJoystickEvents(struct JoystickEvent *jse);
