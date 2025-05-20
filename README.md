# raphtory_playground

A playground to test the funcionalities of Raphtory

## Enviroment

We are going to use a local Neo4J database deployment, just for development. It
is possible that the data between development sessions needs to be saved, for
that porpoise configure the `neo4j_data_storage_path` variable.

```shell
neo4j_data_storage_path="$HOME/repositories/STRAST-UPM/raphtory_playground/neo4j-data"
sudo docker run --rm -d \
    -p 7474:7474 -p 7687:7687 \
    --name neo4j-apoc \
    -e NEO4J_AUTH=none \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4J_PLUGINS=\[\"apoc\"\] \
    --volume "$neo4j_data_storage_path":/data \
    neo4j:2025.04.0
```

In this URL [http://localhost:7474/browser/](http://localhost:7474/browser/) 
a web interface is deployed to interact with the database if needed.
