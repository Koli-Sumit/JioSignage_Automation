import pytest


@pytest.mark.flaky(reruns=1)
@pytest.mark.usefixtures("setup", "log_on_failure")
class BaseTest:
    pass

