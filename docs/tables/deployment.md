
<style>
  .md-content__button {
    display: none;
  }
</style>

**This information is also available in** **[list format](/attributes/deployment/)**

| Concept     | Key         | Subkey           | Type                                | Example Value                                  | Comment                                                                                        | Condition   |
|:------------|:------------|:-----------------|:------------------------------------|:-----------------------------------------------|:-----------------------------------------------------------------------------------------------|:------------|
| Description |             |                  |                                     |                                                |                                                                                                |             |
|             | id          |                  | UUID                                | "HOSTID_MYHOST_A"                              | DIGITbrain reference                                                                           | auto        |
|             | name        |                  | String                              | "Ubuntu small"                                 | Short name for the node/device                                                                 | mandatory   |
|             | author      |                  | String                              | "Jay"                                          | Created by                                                                                     | mandatory   |
|             | date        |                  | Date                                | 18.08.2022                                     | Created on                                                                                     | auto        |
| Deployments |             |                  |                                     |                                                |                                                                                                |             |
|             | type        |                  | Enumeration ["cloudbroker", "edge"] | "cloudbroker"                                  | computing centre                                                                               | mandatory   |
|             | cloudbroker |                  | Map[String, String]                 |                                                | Configuration data for a CloudBroker instance                                                  |             |
|             |             | deployment_id    | UUID                                | "16b1e2d4-3a2c-406e-8c45-5637099021f0"         | ID of CloudBroker Deployment                                                                   | optional    |
|             |             | instance_type_id | UUID                                | "ca727925-a5ca-4697-b2c3-8788d82457d5"         | ID of CloudBroker InstanceType                                                                 | optional    |
|             |             | key_pair_id      | UUID                                | "ap207925-a5ca-4697-b2c3-5637099021f0"         | ID of CloudBroker Key Pair                                                                     | optional    |
|             |             | opened_port      | String (comma separated integers)   | "80,443,8080,30010"                            | Ports to open at cloud side                                                                    | optional    |
|             |             | endpoint         | URL                                 | "https://cloudsme-cbp.scaletools.com.ua"       | Endpoint of the CB Platform                                                                    | optional    |
|             |             | domain_names     | List of UUIDs                       | ["om207925-b52a-4697-b2c3-563702208h9"]        | ID of a CloudBroker Domain Name for this instance                                              | optional    |
|             |             | cloud_config     | Map                                 | {<br>  "runcmd": ["echo one", "echo two"]<br>} | cloud-init - https://cloudinit.readthedocs.io/ - configuration for contextualisation of the VM | optional    |
|             | edge        |                  | Map[String, String]                 |                                                | Connection data for a bring-your-own edge                                                      |             |
|             |             | endpoint         | URL                                 |                                                | accesible IP or FQDN of edge device                                                            | optional    |
|             |             |                  |                                     |                                                |                                                                                                |             |