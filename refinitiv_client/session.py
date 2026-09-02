import os
import lseg.data as ld

_session = None


def open_session() -> None:
    """
    Opens a platform (cloud) session using credentials from environment variables.
    Call once at the start of your script.

    Required env vars:
        LSEG_APP_KEY
        LSEG_USERNAME
        LSEG_PASSWORD
    """
    global _session
    _session = ld.session.platform.Definition(
        app_key=os.environ["LSEG_APP_KEY"],
        grant=ld.session.platform.GrantPassword(
            username=os.environ["LSEG_USERNAME"],
            password=os.environ["LSEG_PASSWORD"],
        ),
        signon_control=True,
    ).get_session()
    ld.session.set_default(_session)
    _session.open()


def close_session() -> None:
    """Closes the active session. Call at the end of your script."""
    global _session
    if _session is not None:
        _session.close()
        _session = None