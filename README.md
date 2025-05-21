# raphtory_playground

A playground to test the functionalities of Raphtory

## Environment

As this is a playground testing environment all the databases that simulates a
production environment are going to be deployed locally using containers but
with persistent data volumes. The `docker-compose.yml` file describes all the
deployment. Use the following command to start:

```shell
sudo docker compose up -d
```

And the following one for stop the service. If you add the option `-v` it will
destroy the defined volumes.

```shell
sudo docker compose down
```

### TimescaleDB

- [Database deployment documentation](
https://docs.timescale.com/self-hosted/latest/install/installation-docker/)
- [Web administrator deployment documentation](
  https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)

In this [URL](http://localhost:8080/) a web interface is deployed to interact
with the database if needed. For login into the administration service use
`user@email.com` and `password` as the credentials. 

When configuring the
timescaledb connection use the name of the service in `docker-compose.yml` file
as the address to reach the service. The default one is `timescaledb`.

### Neo4J

In this [URL](http://localhost:7474/browser/) a web interface is deployed to
interact with the database if needed. No user or password is needed.
