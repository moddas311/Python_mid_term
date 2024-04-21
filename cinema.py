class Star_Cinema:
    
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        seats = []
        for _ in range(self.rows):
            seat_row = []
            for _ in range(self.cols):
                seat_row.append(0)
            seats.append(seat_row)
            self.seats[id] = seats
      

    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print('Invalid id')
            return

        for row, col in seat_list:
            
            if not (1 <= row <= self.rows and 1 <= col <= self.cols):
                print('Selected seat is not valid!')
                continue
            
            if self.seats[show_id][row - 1][col - 1] != 0:
                
                print('Seat already booked.')
                continue
            
            self.seats[show_id][row - 1][col - 1] = 1

    def view_show_list(self):
        
        print('Running Show: ', self.hall_no)
        print()
        for show in self.show_list:
            print(f'Id: {show[0]}, Movie: {show[1]}, Time: {show[2]}')

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print('Invalid id')
            return

        print(f'Available seats for movie {show_id}:')
        
        for row in range(self.rows):
            for seat in self.seats[show_id][row]:
             print(seat, end=' ')
             print()


    def _get_show_by_id(self, show_id):
        
        for show in self.show_list:
            if show[0] == show_id:
                return show
        print('Invalid id')
        return None

    def run(self):
        
        print('<--------------STAR CINEMA------------->')
        
        while True:
            print('\n\t1. View Running movies')
            print('\t2. View available seat for movie')
            print('\t3. Book seat')
            print('\t4. Exit')
            
            option = int(input('\tEnter a option: '))

            if option  == 1:
                self.view_show_list()
                
            elif option == 2:
                show_id = input('Enter movie id: ')
                self.view_available_seats(show_id)
                
            elif option == 3:
                show_id = input('Enter movie id: ')
                show = self._get_show_by_id(show_id)
                if show:
                    row = int(input('Enter row number: '))
                    col = int(input('Enter column number: '))
                    seat_list = [(row, col)]
                    self.book_seats(show_id, seat_list)
                    
            elif option == 4:
                print('Thank You!')
                break
            
            else:
                print('You should choice your option 1-4')


Cineplex = Hall(4, 6, 101)

Cineplex.entry_show('1001', '12th Fail', '15:00')
Cineplex.entry_show('1002', 'Dunki', '18:00')
Cineplex.entry_show('1003', 'Salar', '21:00')

Cineplex.run()