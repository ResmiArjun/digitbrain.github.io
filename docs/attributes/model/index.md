<style>
  .md-content__button {
    display: none;
  }
</style>
# Model Fields

**This information is also available in [table format](/tables/model/)**


## Available Fields 

The metadata specification for a DIGITbrain Model
has these sections:

- [Administrative Data](#administrative-data)
- [Description](#description)
- [Parameters](#parameters)
- [OS Requirements](#os-requirements)
- [Hardware Requirements ](#hardware-requirements-)


### Administrative Data


`ID`{ #id }
:   **Auto-generated**-*ID*- Unique identifier of the asset.

    === "Example"
        ``` yaml     
        "MODID_MYMODEL"
        ```

`AUTHOR`{ #author }
:   **Auto-generated**-*ID*- Unique identifier of the user who created this record

    === "Example"
        ``` yaml     
        UUID
        ```

`PROVIDER`{ #provider }
:   **Auto-generated**-*ID*- Legal entity who provides the asset (owner). It is the affiliation of the author by default.

    === "Example"
        ``` yaml     
        UUID
        ```

`BUILD`{ #build }
:   **Auto-generated**-*Integer*- Build number, incremented automatically to provide versioning for the asset

    === "Example"
        ``` yaml     
        21
        ```

`DATE`{ #date }
:   **Auto-generated**-*DATE (ISO 8601)*- Date of asset registration.

    === "Example"
        ``` yaml     
        2022-04-28T08:11:53+00:00
        ```


### Description


`Name`{ #name }
:   **Required**-*string*- Name of the model


`Version`{ #version }
:   **Optional**-*string*- Version of the model, defined by the provider. 
    === "Example"
        ``` yaml     
        "0.1"
        ```

`License`{ #license }
:   **Optional**-*enum*- License of the model.  Type tbd in SAD group

`Provider_contacts`{ #provider_contacts }
:   **Optional**-*obj*- Dictionary with keys being phone, email, address - Type takes into account co-simulation models, for which solver info is mandatory (next slide)

`Marketplace_description`{ #marketplace_description }
:   **Optional**-*string*- Model tag description Additional info about model files (e.g. versioning, scope, i.e. what is the model used for, e.g. simulation, control, etc.) - Human readable marketplace description

`AuthTool`{ #authtool }
:   **Optional**-*enum*- Authoring Tool used to create the model

`Type`{ #type }
:   **Optional**-*enum*- ML, LCA, 3D FEM and CFD, System simulation, discrete event simulation, co-simulation (it couples a model with specific algorithms) - The original term Path was proposed to be changed (SAD)

`Fidelity`{ #fidelity }
:   **Optional**-*number*- Error of the model’s prediction

`REPOSITORY_URI`{ #repository_uri }
:   **Required**-*URI*- Where the model file is stored (usually the DigitBrain certified external model repository). The path and model filename are not provided via this field.

    === "Example"
        ``` yaml     
        "https://www.myrepo.com"
        ```

`PATH`{ #path }
:   **Required**-*string*- Path to the model file in the specified repository, not including the filename itself.

    === "Example"
        ``` yaml     
        "input/models"
        ```

`FILENAME`{ #filename }
:   **Required**-*string*- Name of the model file at the given path within the given repo, with a file extension if it exists.

    === "Example"
        ``` yaml     
        "mymodel.pb"
        ```

`State_depend`{ #state_depend }
:   **Optional**-*bool*- stateful -> 1, stateless -> 0


### Parameters


`inSlots`{ #inslots }
:   **Optional**-*[Slots](../slots.md)*- List of objects with values on which the model is evaluated (or parameters that might set before or during the evaluation) - Inputs and parameters together, although if needed we can still differentiate them internally in key field for each specific model.
    === "Example"
        ``` yaml     
        [
              { 
                "Key": "MY_INSLO_A",
                "Name": "ModelABin",
                "Dimensions": 112,
                "Is-continuous": true,
                "Units": {
                    "Unit": "Pa",
                    "Exponent": [1, -2, 0],
                    "Offset": 442,
                    "Scale": 10^-3
                },
                "Default-value": 55,
                "Ranges": [1,120]
              }
            ]  
        ```

`outSlots`{ #outslots }
:   **Optional**-*[Slots](../slots.md)*- List of objects with values that the model approximates
    === "Example"
        ``` yaml     
        [
              { 
                "Key": "MY_OUTPUT_A",
                "Name": "ModelABout",
                "Dimensions": 112,
                "Is-continuous": true,
                "Units": {
                    "Unit": "Pa",
                    "Exponent": [1, -2, 0],
                    "Offset": 442,
                    "Scale": 10^-3
                },
                "Default-value": 55,
                "Ranges": [1,120]
              }
            ]  
        ```


### OS Requirements


`osArch`{ #osarch }
:   **Optional**-*enum*- OS architecture type (e.g. x86_64)

`osType`{ #ostype }
:   **Optional**-*enum*- OS type (e.g. Windows, Linux)

`osDistribution`{ #osdistribution }
:   **Optional**-*enum*- OS distributun (e.g. Ubuntu, Fedora)


### Hardware Requirements 


`recommendedNumberOfGPUCores`{ #recommendednumberofgpucores }
:   **Optional**-*number*- Recommended number of GPU cores

`minimumNumberOfGPUCores`{ #minimumnumberofgpucores }
:   **Optional**-*number*- Minimum required number of GPU cores

`recommendedGPURAM`{ #recommendedgpuram }
:   **Optional**-*number*- Recommended GPU memory

`minimumGPURAM`{ #minimumgpuram }
:   **Optional**-*number*- Minimum required GPU memory

`recommendedRAM`{ #recommendedram }
:   **Optional**-*number*- Recommended Memory

`minimumRAM`{ #minimumram }
:   **Optional**-*number*- Minimum required memory

`recommendedCPUs`{ #recommendedcpus }
:   **Optional**-*number*- Recommended number of CPU cores

`minimumCPUs`{ #minimumcpus }
:   **Optional**-*number*- Minimum required number of CPU cores

`requiredDiskSpace`{ #requireddiskspace }
:   **Optional**-*number*- Required amount of disk space in GB
