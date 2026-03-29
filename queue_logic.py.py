class Ticket:
    """Represents a customer's spot in the queue."""
    def __init__(self, ticket_id, customer_name, service_name, est_wait_time):
        self.ticket_id = ticket_id        # [cite: 122]
        self.customer_name = customer_name
        self.service_name = service_name
        self.status = "Waiting"           # [cite: 122]
        self.est_wait_time = est_wait_time # [cite: 122]

    def display_ticket(self):
        print("\n--- DIGITAL TICKET ---")
        print(f"Ticket Number: #{self.ticket_id}") # [cite: 142]
        print(f"Customer: {self.customer_name}")
        print(f"Service: {self.service_name}")
        print(f"Status: {self.status}")
        print(f"Estimated Wait Time: ~{self.est_wait_time} mins") # [cite: 143]
        print("----------------------\n")


class SmartQueueSystem:
    """Core logic for managing the queue."""
    def __init__(self):
        self.queue = []                   # Represents the Customer Queue [cite: 37]
        self.ticket_counter = 1000
        # Simulating Average Service Time from the Service Class [cite: 82]
        self.avg_service_time_mins = 5    

    def join_queue(self, customer_name, service_name):
        """Customer accesses system, selects service, and gets a ticket."""
        # Calculate queue position and estimate wait time 
        position_in_line = len(self.queue)
        est_wait = position_in_line * self.avg_service_time_mins

        # Generate ticket [cite: 127]
        self.ticket_counter += 1
        new_ticket = Ticket(self.ticket_counter, customer_name, service_name, est_wait)
        
        self.queue.append(new_ticket)
        print(f"[SYSTEM] {customer_name} joined the queue. Position: {position_in_line + 1}.")
        return new_ticket

    def call_next_customer(self):
        """Staff action to call the next person in line."""
        if not self.queue:
            print("[STAFF] The queue is currently empty.")
            return None

        # FIFO Logic: Get the first person in the queue
        current_ticket = self.queue.pop(0)
        current_ticket.status = "In Service"
        
        print(f"[STAFF] Calling Next Customer: Ticket #{current_ticket.ticket_id} ({current_ticket.customer_name})") # [cite: 129]
        return current_ticket

    def mark_as_served(self, ticket):
        """Staff action to complete the service."""
        if ticket:
            ticket.status = "Completed"
            print(f"[STAFF] Service for Ticket #{ticket.ticket_id} marked as Completed.") # [cite: 131]
            # In a full system, this would update data logs for the Analytics Dashboard [cite: 149]


# ==========================================
# MAIN APPLICATION LOGIC (SIMULATION)
# ==========================================
if __name__ == "__main__":
    sqms = SmartQueueSystem()

    print("=== 1. CUSTOMERS JOINING QUEUE ===")
    # Customers select a service and get digital tickets [cite: 146]
    ticket1 = sqms.join_queue("Alice Smith", "Banking Service")
    ticket1.display_ticket()

    ticket2 = sqms.join_queue("Bob Jones", "Consultation")
    ticket2.display_ticket()
    
    ticket3 = sqms.join_queue("Charlie Brown", "Banking Service")

    print("\n=== 2. STAFF PROCESSING QUEUE ===")
    # Staff uses dashboard to call tickets [cite: 148]
    serving_ticket = sqms.call_next_customer()
    
    print("\n... Staff is performing the service ...")
    
    # Post-service, ticket is closed [cite: 149]
    sqms.mark_as_served(serving_ticket)

    print("\n=== 3. CALLING NEXT ===")
    serving_ticket_2 = sqms.call_next_customer()
    sqms.mark_as_served(serving_ticket_2)
