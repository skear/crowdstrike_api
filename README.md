# Crowdstrike API

[![Build Status (master)](https://droneio.yaleman.org/api/badges/yaleman/crowdstrike_api/status.svg)](https://droneio.yaleman.org/yaleman/crowdstrike_api)

Implements some of the functions to interface with the [Crowdstrike APIs](https://assets.falcon.crowdstrike.com/support/api/swagger.html).

Want to contribute? Log an issue or PR on the Repo.

To enable logging, use [loguru](https://github.com/Delgan/loguru) and run `logger.enable("crowdstrike")` in your script.

# Examples

### Create a connection

```falcon_client = crowdstrike.CrowdstrikeAPI(client_id="myid", client_secret="mysecret")```

### Create an IOC

```create = falcon_client.iocs_create(policy = "detect", type = "domain", value = "mydomain.com")```

### Create an IOC

```get = falcon_client.iocs_get(type = "domain", value = "mytest.com")```

### Delete an IOC

```delete = falcon_client.iocs_delete(type = "domain", value = "mydomain.com")```
