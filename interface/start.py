"""Create the window and handle input."""

from threading import Thread
from time import sleep

from interface.display import render, RUNNING
import interface.display

import interface.input

import pygame

# Constants
RESOLUTION = (500, 500)


def _interface_loop():
    """Handle all pygame functionality continuously."""
    pygame.init()

    display = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

    while RUNNING:
        # Render display
        render(display, (0, 0, 0))

        # Handle events
        events = pygame.event.get()
        display = interface.display.check_events(display, events)

        interface.input.check_events(events)

        pygame.display.flip()
        sleep(.01)


def init():
    """Create the display and handle all related functionality."""
    interface_thread = Thread(target=_interface_loop)
    interface_thread.setDaemon(True)
    interface_thread.start()


def get_running():
    """Check if the interface has been closed by the user or stopped."""
    # TODO: check if any important threads have terminated
    return interface.display.RUNNING
