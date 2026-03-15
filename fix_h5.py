import h5py
import json

def fix_h5(file_path):
    with h5py.File(file_path, 'r+') as f:
        # Check if 'model_config' exists in attributes
        if 'model_config' in f.attrs:
            model_config = json.loads(f.attrs['model_config'])
            
            # Helper function to remove quantization_config recursively
            def remove_qc(config):
                if isinstance(config, dict):
                    if 'quantization_config' in config:
                        del config['quantization_config']
                    for k, v in config.items():
                        remove_qc(v)
                elif isinstance(config, list):
                    for item in config:
                        remove_qc(item)

            remove_qc(model_config)
            
            # Save the modified config back
            f.attrs['model_config'] = json.dumps(model_config).encode('utf-8')
            print("Successfully removed 'quantization_config' from model_config.")
        else:
            print("No 'model_config' found in the H5 file.")

if __name__ == "__main__":
    fix_h5('cats_dogs_model.h5')
