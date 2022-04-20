import rospy
from std_msgs.msg import String

def rev_sentence(sentence): 
  
    words = sentence.split(' ') 
  
    reverse_sentence = ' '.join(reversed(words)) 
  
    return reverse_sentence
    
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def callback(data):
    snew=rev_sentence(data.data)
    snewnew=reverse(snew)
    rospy.loginfo('%s', snewnew)


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('team_abhiyaan', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
