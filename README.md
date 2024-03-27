# EXAMPLE WORKFLOW

This is a simple snakemake worflow that demonstrates how to use snk. 

# Installation 

```bash
snk install wytamma/snk-basic-pipeline
```

# Usage

Download the example data

```bash
snk-basic-pipeline script run download_data
```

Run the workflow

```bash
snk-basic-pipeline run 
```

Configure the workflow

```bash
snk-basic-pipeline run --sample A --sample B
```