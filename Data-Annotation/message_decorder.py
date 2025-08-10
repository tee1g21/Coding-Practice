import urllib.request
from bs4 import BeautifulSoup as bs
       
def message_decoder(url):
    parsed_table = parse_google_doc(url)
    
    max_x = max(parsed_table[0])
    max_y = max(parsed_table[2])
    
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
   
    for x, char, y in zip(*parsed_table):
        grid[y][x] = char
    
    pretty_print(grid)   
    #print(grid)
           
def parse_google_doc(url): 
    contents = urllib.request.urlopen(url).read()
    
    soup = bs(contents, "html.parser")
       
    table = soup.select_one("#contents>div>table")

    if not table: 
        raise Exception("Unexpected Format")
    
    parsed_table = [[],[],[]]
    
    for i, table_row in enumerate(table.children):    
        if i == 0: 
            continue          
        
        if not table_row: 
            raise Exception("Unexpected Format")
        
        for j, table_data in enumerate(table_row.children): # type:ignore
            cell = table_data.p.span.get_text()
            
            if j != 1: 
                cell = int(cell)    
                
            parsed_table[j].append(cell)
    
    return parsed_table

    
def pretty_print(grid):
    
    # reversed to match coordinate system. 0,0 bottom left. 
    for i in reversed(range(len(grid))): 
        for j in range(len(grid[0])): 
            print(grid[i][j], end="")
            
        print("\r")

if __name__ == "__main__":
    message_decoder("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")