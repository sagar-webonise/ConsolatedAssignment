import urllib2
import simplejson
  
def main():     
    req = urllib2.Request("http://blooming-beach-2334.herokuapp.com/users.json")
    opener = urllib2.build_opener()
    f = opener.open(req)
    jfile=open("user.json","w")
    jfile.write(f.read())
    jfile.close()   


if __name__ == "__main__":
    main()
