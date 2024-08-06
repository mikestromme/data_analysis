import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import io
import os
from collections import defaultdict

def analyze_csv(csv_content, filename):
    # Read the CSV content
    df = pd.read_csv(io.StringIO(csv_content.decode('utf-8')), parse_dates=['Time'])
    
    # Calculate statistics for oxygen levels
    stats = {
        'mean': df['Oxygen Level'].mean(),
        'median': df['Oxygen Level'].median(),
        'min': df['Oxygen Level'].min(),
        'max': df['Oxygen Level'].max(),
        'std': df['Oxygen Level'].std()
    }
    
    return stats, df

def process_zip_file(zip_filepath):
    all_stats = defaultdict(list)
    all_data = pd.DataFrame()

    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        for filename in zip_ref.namelist():
            if filename.endswith('.csv'):
                with zip_ref.open(filename) as file:
                    csv_content = file.read()
                    stats, df = analyze_csv(csv_content, filename)
                    
                    for key, value in stats.items():
                        all_stats[key].append(value)
                    
                    all_data = pd.concat([all_data, df])

    # Calculate overall statistics
    overall_stats = {key: pd.Series(values).agg(['mean', 'min', 'max']) for key, values in all_stats.items()}

    # Print summary
    print("\nOverall Oxygen Saturation Statistics:")
    for stat, values in overall_stats.items():
        print(f"{stat.capitalize()}:")
        print(f"  Average: {values['mean']:.2f}")
        print(f"  Minimum: {values['min']:.2f}")
        print(f"  Maximum: {values['max']:.2f}")

    # # Plot overall oxygen levels
    # plt.figure(figsize=(12, 6))
    # plt.plot(all_data['Time'], all_data['Oxygen Level'], alpha=0.5)
    # plt.title('Overall Oxygen Saturation')
    # plt.xlabel('Time')
    # plt.ylabel('Oxygen Saturation (%)')
    # plt.ylim(90, 100)  # Adjust y-axis to focus on the relevant range
    # plt.grid(True)
    # plot_filename = 'overall_oxygen_saturation_plot.png'
    # plt.savefig(plot_filename)
    # plt.close()
    
    # print(f"\nOverall plot saved as '{plot_filename}'")

# Usage
zip_filepath = 'O2Ring_20230724203820.zip'  # Replace with the actual path to your zip file
process_zip_file(zip_filepath)
