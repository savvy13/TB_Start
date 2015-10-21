# TB_Start
# try to pull file from github to run automatically thru ssh connection

os.system('echo $ export ROS_HOSTNAME=130.215.218.218 >> ~/.bashrc')
print "Hostname set"
os.system('echo $ export ROS_MASTER_URI=130.215.218.213:11311 >> ~/.bashrc')
print "Master set"
