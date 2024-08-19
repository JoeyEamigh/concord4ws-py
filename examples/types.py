import logging
from concord4ws.types import (
    ArmOptions,
    CommandSendableMessage,
    ConcordArmCommand,
    code_to_keypresses,
)


logger = logging.getLogger("concord4ws")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def main():
    code = "1234"
    print(f"Code: {code}")

    keypress_code = code_to_keypresses(code)
    print(f"Keypress Code: {keypress_code}")

    arm_command = CommandSendableMessage(
        data=ConcordArmCommand(
            params=ArmOptions(
                mode="stay", code=keypress_code, level="instant", partition=1
            )
        )
    )

    arm_command_json = arm_command.json()
    print(f"Arm Command JSON: {arm_command_json}")


main()
