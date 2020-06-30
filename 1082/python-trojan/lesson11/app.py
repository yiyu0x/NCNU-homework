from ftplib import FTP, error_perm
import os


def draw_dir(dir_box):
    print(dir_box[0])
    for i in dir_box[1:]:
        path = os.path.split(i)
        deep = len(path[0].split('/')) - 1
        print('   ' * deep + '|')
        print('   ' * deep + '+---' + path[1])

def walk_dir(ftp, dirpath, dirs=[]):
    original_dir = ftp.pwd()
    try:
        ftp.cwd(dirpath)
    except error_perm:
        return  # ignore non-directores and ones we cannot enter
    dirs.append(dirpath)
    names = sorted(ftp.nlst())
    for name in names:
        walk_dir(ftp, dirpath + '/' + name, dirs) # return to cwd of our caller
    ftp.cwd(original_dir)
    return dirs

def main():
    serverName = 'ftp.ncnu.edu.tw'
    pathName = '/FreeBSD'
    ftp = FTP(serverName)
    ftp.login()
    dir = walk_dir(ftp, pathName)
    draw_dir(dir)
    ftp.quit()

main()