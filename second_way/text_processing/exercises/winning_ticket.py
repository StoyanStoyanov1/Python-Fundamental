class WinningTicket:
    _checked_tickets = []

    def __init__(self, current_tickets):
        self.current_tickets = current_tickets
        self.symbols = ["@", "#", "$", "^"]
        self.ticket_check()

    def ticket_check(self):
        for ticket in self.current_tickets:
            ticket_is_winning = False
            if len(ticket) != 20:
                self._checked_tickets.append("invalid ticket")
                continue

            left_part = ticket[:10]
            right_part = ticket[10:]
            for symbol in self.symbols:
                if ticket_is_winning:
                    break
                for length_symbol in range(10, 5, -1):
                    win_symbols = length_symbol * symbol
                    if win_symbols in left_part and win_symbols in right_part:
                        ticket_is_winning = True
                        if length_symbol == 10:
                            self._checked_tickets.append(f'ticket "{ticket}" - 10{symbol} Jackpot!')
                        else:
                            self._checked_tickets.append(f'ticket "{ticket}" - {length_symbol}{symbol}')
                        break

            if not ticket_is_winning:
                self._checked_tickets.append(f'ticket "{ticket}" - no match')

    def return_checked_tickets(self):
        return "\n".join(self._checked_tickets)


tickets = [ticket.strip() for ticket in input().split(",")]
winning_ticket = WinningTicket(tickets)
print(winning_ticket.return_checked_tickets())