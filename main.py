
import sys
sys.path.insert(0, 'lib')
import webapp2
import paste
import keyword_extraction
# import twitter_streaming
import price_extraction

############-----------WEB APP CODE-------------------###########
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("Welcome to Addison\'s web app.")
        self.response.write("""
          <html>
            <head><title>Keywords & Performance</title></head>
            <body>
              <form action="/prices" method="post">
                <input type="text" name="data_1"><br>
                <input type="submit" value="View Stock Prices">
              </form>
            </body>
            </html>""")

class Prices(webapp2.RequestHandler):
    def post(self):
      self.response.headers["Content-Type"] = "text/html"
      self.response.write("""
          <html>
            <head><title>Streaming</title></head>
            <body>
            Here are today's stock price changes: """)
      price_extraction.extract()
      self.response.write(price_extraction.price_changes)
      self.response.write(""" <tb> The average change: """)
      self.response.write(price_extraction.avg_change)
      self.response.write("""
              <form action="/" method="get">  
                <input type="submit" value="Return">
              </form>
            </body>
            </html>""")
      

#########-------------PYTHON METHODS-----------------############

routes = [('/', MainPage), ('/prices', Prices)]


app = webapp2.WSGIApplication(routes, debug=True) 

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()

# import time
# print start = time.time()

# if (time.time()-start > 5000):
#   break
