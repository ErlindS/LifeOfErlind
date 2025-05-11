## Function Inhibition Manager (FIM)
- Application functionality is executed conditionally.
    - Depending on error memory contents  
         (diagnostic events).
- Gets current failure status from DEM.
- Sets inhibition status for a configurable number of DEM events.
- Inhibition status is polled by Application (_Fim_GetFunctionPermission_).

## Diagnostic Event Manager (DEM)
- Error memory
    - Saves diagnostic events from BSW and Application.

## Diagnostic Communication Manager (DCM)
- Implements the diagnostic communication protocol.
- Is Bus independent.