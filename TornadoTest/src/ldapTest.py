import ldap

ldapConn = ldap.initialize("ldap://127.0.0.1")
ldapConn.protocol_version = 3
ldapConn.set_option(ldap.OPT_REFERRALS, 0)

try:
    ldapConn.simple_bind_s("cn=etlx82x,dc=test,dc=com", "logic123#")
    print "User Successfully Connected..."
except ldap.LDAPError:
    print "Invalid Username or Password..."
