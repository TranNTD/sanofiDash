# batch_analysis.py
import pandas as pd

def find_batch_indices(df, time):
    """
    Finds the start and end indices for each batch in the DataFrame.
    """
    batch_end_indices = df[df['Time (h)'] == time].index - 1
    batch_end_indices = batch_end_indices[batch_end_indices > 0]
    batch_end_indices = batch_end_indices.append(pd.Index([df.index[-1]]))

    batch_start_indices = df['Time (h)'].index[df['Time (h)'] == time]
    batch_indices = []
    batch_start = batch_start_indices[0]
    
    for batch_end in batch_end_indices:
        batch_indices.append((batch_start, batch_end))
        batch_start = batch_end + 1

    return batch_indices

def get_batch_data(df, batch_number, batch_indices):
    """
    Retrieves the data for a specified batch.
    """
    if 1 <= batch_number <= len(batch_indices):
        batch_start, batch_end = batch_indices[batch_number - 1]
        batch_df = df.loc[batch_start:batch_end]
        return batch_df
    else:
        raise ValueError(f"Batch {batch_number} is out of range.")

