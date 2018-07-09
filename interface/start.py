"""Create the window and handle input."""

from threading import Thread
from time import sleep

from interface.display import render, running
import interface.display

import interface.input

import pygame

# Constants
RESOLUTION = (500, 500)


def _interface_loop():
    """Handle all pygame functionality continuously."""
    pygame.init()

    display = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

    while running:
        # Render display
        render(display)

        # Handle events
        events = pygame.event.get()
        display = interface.display.check_events(display, events)

        interface.input.check_events(events)

        pygame.display.flip()  # TODO: only render on change; mark dirty
        sleep(.01)


def init():
    """Create the display and handle all related functionality."""
    interface_thread = Thread(target=_interface_loop)
    interface_thread.setDaemon(True)
    interface_thread.start()


def get_running():
    """Check if the interface has been closed by the user or stopped."""
    # EVENTUALLY: check if any important threads have terminated
    return interface.display.running