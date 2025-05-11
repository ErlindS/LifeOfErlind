
# WdgM
**Functionalities**
- Manages alive indications from all supervised entities (Runnables of application).
- Interacts with your application and offers you to supervise the execution of your software in many different ways.
- Derives Global Supervision Status.
- Triggers WdgIf if Runnables behave like expected.
**Example**
- With the Watchdog Manager (WdgM) deadline monitoring, live supervision etc. are possible.
# Wdglf
**Functionality**
- Triggers Hardware Watchdog(s)
# WdgDrv
**Functionality**
- Internal or external Watchdog driver.

Runnables can register to a watchdog manager. They have to inform the Watchdog Manager in a certain amount of time that they are up and running. If this happens, the watchdog manager informs the watchdog driver that everything is OK and the timer will be restarted.

If not all registered runnables are calling the watchdog manager, the watchdog manager is not able to inform the watchdog driver. In that case, the timer ends and the whole ECU will be restarted.