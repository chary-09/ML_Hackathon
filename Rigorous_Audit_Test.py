from Task_2_Model_Development.model.compute_metrics import eval_dataset
import os


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "Task_1_Data_Preprocessing", "data")
    dataset_files = [
        "indian_student_burnout_dataset_120.csv",
        "student_burnout_dataset_2000_fixed.csv",
        "student_burnout_dataset_5000.csv",
    ]

    print("Rigorous audit across available datasets")
    print("-" * 45)

    for file_name in dataset_files:
        dataset_path = os.path.join(data_dir, file_name)
        metrics = eval_dataset(dataset_path)
        print(f"\nDataset: {file_name}")
        for model_name, scores in metrics.items():
            print(f"  {model_name}")
            for metric_name, value in scores.items():
                print(f"    {metric_name}: {value:.2f}%")


if __name__ == "__main__":
    main()
