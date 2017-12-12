import tornado.web
import tornado.ioloop
import utils
import ldap
import settings;


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        student = utils.Student()    
        self.render("index.html", studentInfo=student.getStudentDetails())


class LoginHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.render("login.html")
        
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        ldapConn = ldap.initialize(settings.ldapServer);
        ldapConn.protocol_version = 3
        ldapConn.set_option(ldap.OPT_REFERRALS, 0)
        
        try:
            ldapConn.simple_bind_s("cn=" + username + "," + settings.ldapBaseDn, password)
            self.write("Welcome: %s" % username)
        except ldap.LDAPError:
            self.write("Login Denied...")
        
def make_app():
    handlers = [(r"/", MainHandler,),
                (r"/login", LoginHandler), ]
    settings = {'autoreload': True, 'template_path':'/home/manu/My_Workspace/TornadoTest/templates'}
    
    return tornado.web.Application(handlers, **settings)


if __name__ == '__main__':
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
    
