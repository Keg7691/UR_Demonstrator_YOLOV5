import socket

def send_urscript(script, host):
    port = 30002  # UR secondary client port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(script.encode('utf-8'))
    s.close()

# URScript file content
urscript = """
def move_to_position():
    movel(p[-0.37221, -0.01232, 0.559, 2.944, -1.163, 0.023], a=0.1, v=0.10)
    textmsg("Movement complete!")
end

move_to_position()
"""

# Robot IP address
robot_ip = '192.168.2.180'

# Send URScript to the robot
send_urscript(urscript, robot_ip)
