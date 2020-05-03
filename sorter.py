
class Sorter:

    def __init__(self, tickets):
        self.tickets = tickets


    def journeyStartEnd(self):
        all_start_tickets, all_finish_tickets = list(), list()
        from_tickets, to_tickets = list(), list()
         

        # In case of no tickets in the list:
        if len(self.tickets) == 0:
            return None

        for current_ticket in self.tickets:
            # Putting all data about starts and destinations.
            all_start_tickets.append(current_ticket['start'])
            all_finish_tickets.append(current_ticket['finish'])

            # Finding tickets that have some connection to other ones.
            for other_ticket in self.tickets:
                if current_ticket['start'] == other_ticket['finish']:
                    from_tickets.append(current_ticket['start'])

                if current_ticket['finish'] == other_ticket['start']:
                    to_tickets.append(current_ticket['finish'])

        # Finding start and finish of the journey.
        start_from = list(
                        set(all_start_tickets).difference(set(from_tickets))
                        )

        finish_on = list(
                        set(all_finish_tickets).difference(set(to_tickets))
                        )


        # In case of tickets that would not create correct path.
        # There should be one start and one finish.
        if len(start_from) + len(finish_on) > 2:
            return None

        # Finding specific tickets that got found start and finish.
        start_from_ticket = [ticket for ticket in self.tickets if ticket['start'] == start_from[0]]
        finish_on_ticket = [ticket for ticket in self.tickets if ticket['finish'] == finish_on[0]]

            
        return start_from_ticket[0], finish_on_ticket[0]

    def makeConnections(self):
        try: 
            start_point, finish_point = self.journeyStartEnd()

            # Finding tickets that are not first in the path.
            other_tickets = [ticket for ticket in self.tickets if ticket is not start_point]

            # Initializing list with very first ticket.
            path = [start_point]

            while 1==1:
                for ticket in other_tickets:
                    # Adding ticket to the path based on start - finish connection.
                    if ticket['start'] == path[-1]['finish']:
                        path.append(ticket)

                # Break loop if final ticket joins the path.
                if finish_point in path:
                    break

            return path
        except:
            # In case of incorrect input (no tickets or tickets without connection)
            return None