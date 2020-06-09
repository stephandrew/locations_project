import csv

atx_todo = 'austin_places.csv'

print('read or write')
user_in = input()

if user_in == 'write':

    with open(atx_todo, 'a', newline='') as csv_writer:
            # list header names
            fieldnames = ['location_name', 'category', 'description', 'rating', 'visited']

            # This opens the `DictWriter`. Notice that we pass in the list of fieldnames
            writer = csv.DictWriter(csv_writer, fieldnames)

            # Write out the header row (this only needs to be done once!) writer.writeheader()

            location_name = ' '
            category = ' '
            description = ' '
            rating = 0

            # Write as many rows as you want!
            
            while location_name != 'exit':
                print('location name')
                location_name = input()

                for row in csv.writer(csv_writer):
                    if location_name != row['id']:
                        print('category name')
                        category = input()

                        print('notes')
                        description = input()

                        print('visited')
                        visited = input()
                        
                        if visited == 'Yes':
                            visit = 'Yes'
                            print('rating')
                            rate = input()

                        writer.writerow(row)

                    else:
                        print("Avatar Record Deleted")
            
                if category == 'exit':
                    csv_writer.close()
                    print('writer closed')

elif user_in == 'read':
    with open(atx_todo, 'r', newline='') as csv_reader:
         print('what are you looking for today?')
         input_category = input()
         print('\n')

         for row in csv.reader(csv_reader):
             if row[1] == input_category:
                 print(row[0])