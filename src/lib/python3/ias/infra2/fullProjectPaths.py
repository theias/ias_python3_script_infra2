import os
import pprint

class IASInfraFullProjectPaths:
    def do_base_path_calculations(self):
        if self.are_we_in_src():
            self.up_path_components=['..']
            self.project_name=self.script_path_components[-3]
        elif self.are_we_in_local_bin():
            self.up_path_components=['..']
        elif self.are_we_in_ias_venv():
            self.up_path_components=['..','..','..']
            self.installed_package_name=self.script_path_components[-2]
        else:
            self.installed_package_name=self.script_path_components[-1]
            self.up_path_components=['..','..']
    
        
    
    def get_generic_project_directory(self, dir_name):
        if self.are_we_in_src():
            join_args = [self.paths[self.bin_whence]]
            join_args.extend(self.up_path_components)
            join_args.append(dir_name)
            # print("src...")
            return os.sep.join(join_args)
        elif self.are_we_in_local_bin():
            join_args = [self.paths[self.bin_whence]]
            join_args.extend(self.up_path_components)
            join_args.append(dir_name)
            # print("local")
            return os.sep.join(join_args)
        else:
            join_args = [self.paths[self.bin_whence]]
            join_args.extend(self.up_path_components)
            join_args.append(dir_name)
            join_args.append(self.installed_package_name)
            # print("installed")

            return os.sep.join(join_args)

    def bin_dir(self):
        return self.paths[self.bin_whence]
    
    def input_dir(self):
        return self.get_generic_project_directory('input')

    def output_dir(self):
        return self.get_generic_project_directory('output')

    def conf_dir(self):
        return self.get_generic_project_directory('etc')
    
    def log_dir(self):
        return self.get_generic_project_directory('log')

    def script_output_dir(self):
        project_output_dir = self.output_dir()
        script_output_dir = os.sep.join([
            project_output_dir,
            self.script_name_without_extension
        ])
        
        return script_output_dir
