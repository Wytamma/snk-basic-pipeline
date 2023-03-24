import argparse
import pandas as pd
import altair as alt
from pysam import VariantFile

def plot(input, output):

    quals = pd.DataFrame({"qual": [record.qual for record in VariantFile(input)]})

    chart = alt.Chart(quals).mark_bar().encode(
        alt.X("qual", bin=True),
        alt.Y("count()")
    )

    chart.save(output)

if __name__ == "__main__":
    snakemake = globals().get('snakemake')
    if snakemake:
        plot(snakemake.input[0], snakemake.output[0])
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('input') 
        parser.add_argument('output') 
        args = parser.parse_args()
        plot(args.input, args.output)
