import pygame
from pygame.locals import *


def ESC_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the ESC key is pressed."""
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    return True


def SPACEBAR_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the SPACEBAR key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        return True
    return False


def BACKSPACE_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the BACKSPACE key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        return True
    return False


def RETURN_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the RETURN key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        return True
    return False


def STAR_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the STAR key is pressed.
    """
    if event.type == pygame.KEYDOWN and (
        event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_ASTERISK
    ):
        return True
    return False


def TAB_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the TAB key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
        return True
    return False


def K_UP_func(event: pygame.event) -> bool:
    """
    Returns True if the UP key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        return True
    return False


def K_DOWN_func(event: pygame.event) -> bool:
    """
    Returns True if the DOWN key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        return True
    return False


def K_LEFT_func(event: pygame.event) -> bool:
    """
    Returns True if the LEFT key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        return True
    return False


def K_RIGHT_func(event: pygame.event) -> bool:
    """
    Returns True if the RIGHT key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        return True
    return False

def PLUS_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the PLUS key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_PLUS:
        print('bruh')
        return True
    return False

def MINUS_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the MINUS key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS:
        return True
    return False

def S_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the S key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        print('bruh')
        return True
    return False

def R_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the R key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        return True
    return False

def P_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the P key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
        return True
    return False

def M_KEYDOWN(event: pygame.event) -> bool:
    """
    Returns True if the M key is pressed.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
        return True
    return False