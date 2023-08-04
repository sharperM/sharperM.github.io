

# 遍历 sql目录
# 读取 sql文件
# 执行 sql文件
# 打印执行结果
# 打印执行时间

import os
import time

host = '127.0.0.1'
port = 3306
user = 'sealy'
password = '123456'
# database = 'your_database_name'


# 读取 sql文件
def readSqlFile(path):
    sqlFile = open(path, 'r', encoding='utf-8')
    sql = sqlFile.read()
    sqlFile.close()
    return sql


# mysql dump < file.sql
def mysqlDump(sql_script_path, database):
    import subprocess

    # Define the command to import the MySQL dump file
    command = 'mysql -uroot -p123456 '+ database +' < ' + sql_script_path

    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print("MySQL dump file import successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while importing the MySQL dump file: {e}")



# 遍历 sql目录
def traverseSqlDir(path):
    ddl = os.listdir(path)
    for i in range(len(ddl)):
        dirpath = os.path.join(path, ddl[i])
        if os.path.isdir(dirpath) and  ddl[i] != ('.git'):
            database = ddl[i]
            test(dirpath,ddl[i])
            # ddl2 = os.listdir(dirpath)
            # print(ddl2)
            # sortddl = sorted(ddl2,key = lambda x:int(x[:-4]))
            # print(sortddl)
    # for root, dirs, files in os.walk(path):
    #     for file in files:
    #         if file.endswith(".sql"):
    #             print(os.path.join(root, file))
                # sql = readSqlFile(os.path.join(root, file))
                
                # executeSql(sql)


# 打印执行结果
def printResult():
    pass


# 打印执行时间
def printTime():
    pass

def test(base_path,database):
    # import os

    # Define the directory path
    # base_path = '/path/to/v'  # Replace this with the common base directory path

    # Generate a list of directories matching the pattern v1 to v11
    dirs = [f for f in os.listdir(base_path) if f.startswith('v') and f[1:].isdigit()]

    # Sort the directories based on numeric values
    sorted_dirs = sorted(dirs, key=lambda x: int(x[1:]))

    # Traverse the sorted directories, excluding directories with the name ".git"
    for dir_name in sorted_dirs:
        full_path = os.path.join(base_path, dir_name)
        if os.path.isdir(full_path) and dir_name != '.git':
            # Your code to perform actions on each directory goes here
            # print(full_path)
            # print(os.listdir(full_path))
            test2(full_path,database)


def test2(base_path,database):
    import re

    # Define the directory path
    # base_path = '/path/to/v'  # Replace this with the common base directory path

    # Generate a list of directories matching the pattern v1 to v11
    dirs = [f for f in os.listdir(base_path) if f.startswith('v') and f[1:2].isdigit() and f[-4:] == '.sql']
    pattern = r'_(\d+).sql'
    # Sort the directories based on numeric values
    sorted_dirs = sorted(dirs, key=lambda x: int(re.search(pattern, x).group(1)))

    # Traverse the sorted directories, excluding directories with the name ".git"
    for dir_name in sorted_dirs:
        full_path = os.path.join(base_path, dir_name)
        print(full_path)
        # executeSql(full_path,database)
        mysqlDump(full_path,database)
        # if os.path.isdir(full_path) and dir_name != '.git':
            # Your code to perform actions on each directory goes here
            # print(full_path)
            # print(os.listdir(full_path))
            # test(full_path)



if __name__ == '__main__':
    # ddl = os.listdir('svr/external/lkgamecore/sql')
    # print(ddl)
    # sssll = sorted(ddl,key = lambda x:int(x[:-2]))
    # print(sssll)
    traverseSqlDir('./sql')
    f = "12345.sql"
    print(f[-5:-4])
    # test()
    printResult()
    printTime()
