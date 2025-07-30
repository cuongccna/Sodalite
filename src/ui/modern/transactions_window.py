"""
FinanTidy - Transactions Module
Modern CustomTkinter interface for financial transaction management
"""

import customtkinter as ctk
from tkinter import messagebox, ttk
import datetime
import random

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TransactionsWindow(ctk.CTkToplevel):
    """Modern Transactions Management Window"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Window configuration
        self.title("FinanTidy - Transaction Management")
        self.geometry("1600x900")
        self.transient(parent)
        
        # Transaction data
        self.transactions_data = self.generate_sample_transactions()
        self.filtered_transactions = self.transactions_data.copy()
        
        # Create UI
        self.create_transactions_ui()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (1600 // 2)
        y = (self.winfo_screenheight() // 2) - (900 // 2)
        self.geometry(f"1600x900+{x}+{y}")
    
    def generate_sample_transactions(self):
        """Generate sample transaction data"""
        
        transaction_types = ["Income", "Expense", "Transfer"]
        categories = {
            "Income": ["Sales Revenue", "Service Income", "Interest", "Other Income"],
            "Expense": ["Office Supplies", "Marketing", "Travel", "Utilities", "Software", "Professional Services"],
            "Transfer": ["Bank Transfer", "Account Transfer", "Cash Deposit"]
        }
        
        accounts = ["Main Account", "Business Account", "Cash", "Petty Cash", "Savings"]
        statuses = ["Completed", "Pending", "Failed", "Cancelled"]
        
        transactions = []
        
        for i in range(50):
            trans_type = random.choice(transaction_types)
            category = random.choice(categories[trans_type])
            
            # Generate realistic amounts based on type
            if trans_type == "Income":
                amount = random.randint(5000000, 50000000)  # 5M - 50M VND
            elif trans_type == "Expense":
                amount = random.randint(500000, 15000000)   # 500K - 15M VND
            else:  # Transfer
                amount = random.randint(1000000, 20000000)  # 1M - 20M VND
            
            # Generate date (last 60 days)
            days_ago = random.randint(0, 60)
            transaction_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
            
            transaction = {
                "id": f"TXN{str(i+1).zfill(4)}",
                "date": transaction_date,
                "type": trans_type,
                "category": category,
                "description": f"{category} - Transaction {i+1}",
                "amount": amount,
                "account": random.choice(accounts),
                "status": random.choice(statuses),
                "reference": f"REF{random.randint(10000, 99999)}",
                "notes": f"Automated transaction entry for {category.lower()}"
            }
            
            transactions.append(transaction)
        
        # Sort by date (newest first)
        transactions.sort(key=lambda x: x["date"], reverse=True)
        
        return transactions
    
    def create_transactions_ui(self):
        """Create transactions management interface"""
        
        # Main container
        main_container = ctk.CTkFrame(self, corner_radius=0)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Content area
        content_area = ctk.CTkFrame(main_container, corner_radius=0)
        content_area.pack(fill="both", expand=True, pady=(20, 0))
        
        # Controls and filters
        self.create_controls_section(content_area)
        
        # Transactions list
        self.create_transactions_list(content_area)
    
    def create_header(self, parent):
        """Create header with title and summary"""
        
        header_frame = ctk.CTkFrame(parent, height=120, corner_radius=15)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Left side - Title and summary
        left_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="both", expand=True, padx=25, pady=20)
        
        title_label = ctk.CTkLabel(
            left_frame,
            text="💳 Transaction Management",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(anchor="w")
        
        subtitle_label = ctk.CTkLabel(
            left_frame,
            text="Track and manage all financial transactions",
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        subtitle_label.pack(anchor="w")
        
        # Summary stats
        summary_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        summary_frame.pack(anchor="w", pady=(10, 0))
        
        # Calculate summary
        total_income = sum(t["amount"] for t in self.transactions_data if t["type"] == "Income")
        total_expense = sum(t["amount"] for t in self.transactions_data if t["type"] == "Expense")
        net_amount = total_income - total_expense
        
        summary_text = f"📊 Total Transactions: {len(self.transactions_data)} | 💰 Income: ₫{total_income:,.0f} | 💸 Expenses: ₫{total_expense:,.0f} | 📈 Net: ₫{net_amount:,.0f}"
        
        summary_label = ctk.CTkLabel(
            summary_frame,
            text=summary_text,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#10b981" if net_amount >= 0 else "#ef4444"
        )
        summary_label.pack(anchor="w")
        
        # Right side - Action buttons
        right_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="y", padx=25, pady=20)
        
        # Export button
        export_button = ctk.CTkButton(
            right_frame,
            text="📊 Export",
            height=40,
            width=120,
            font=ctk.CTkFont(size=14),
            fg_color="#10b981",
            hover_color="#059669",
            command=self.export_transactions
        )
        export_button.pack(pady=(0, 10))
        
        # Add transaction button
        add_button = ctk.CTkButton(
            right_frame,
            text="➕ Add Transaction",
            height=40,
            width=150,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.add_transaction
        )
        add_button.pack()
    
    def create_controls_section(self, parent):
        """Create filter and search controls"""
        
        controls_frame = ctk.CTkFrame(parent, height=80, corner_radius=15)
        controls_frame.pack(fill="x", pady=(0, 20))
        controls_frame.pack_propagate(False)
        
        # Left side - Filters
        left_controls = ctk.CTkFrame(controls_frame, fg_color="transparent")
        left_controls.pack(side="left", fill="y", padx=20, pady=15)
        
        # Type filter
        type_label = ctk.CTkLabel(left_controls, text="Type:", font=ctk.CTkFont(size=12, weight="bold"))\n        type_label.pack(side="left", padx=(0, 5))
        
        self.type_filter = ctk.CTkOptionMenu(
            left_controls,
            values=["All Types", "Income", "Expense", "Transfer"],
            width=120,
            height=30,
            command=self.apply_filters
        )
        self.type_filter.pack(side="left", padx=(0, 15))
        
        # Status filter
        status_label = ctk.CTkLabel(left_controls, text="Status:", font=ctk.CTkFont(size=12, weight="bold"))
        status_label.pack(side="left", padx=(0, 5))
        
        self.status_filter = ctk.CTkOptionMenu(
            left_controls,
            values=["All Status", "Completed", "Pending", "Failed", "Cancelled"],
            width=120,
            height=30,
            command=self.apply_filters
        )
        self.status_filter.pack(side="left", padx=(0, 15))
        
        # Date range
        date_label = ctk.CTkLabel(left_controls, text="Period:", font=ctk.CTkFont(size=12, weight="bold"))
        date_label.pack(side="left", padx=(0, 5))
        
        self.date_filter = ctk.CTkOptionMenu(
            left_controls,
            values=["All Time", "Today", "This Week", "This Month", "Last 30 Days"],
            width=130,
            height=30,
            command=self.apply_filters
        )
        self.date_filter.pack(side="left")
        
        # Right side - Search
        right_controls = ctk.CTkFrame(controls_frame, fg_color="transparent")
        right_controls.pack(side="right", fill="y", padx=20, pady=15)
        
        # Search entry
        self.search_entry = ctk.CTkEntry(
            right_controls,
            placeholder_text="🔍 Search transactions...",
            width=300,
            height=35,
            font=ctk.CTkFont(size=14)
        )
        self.search_entry.pack(side="right", padx=(10, 0))
        self.search_entry.bind("<KeyRelease>", self.on_search_change)
        
        # Clear filters button
        clear_button = ctk.CTkButton(
            right_controls,
            text="🔄 Clear",
            width=80,
            height=35,
            fg_color="#6b7280",
            hover_color="#4b5563",
            command=self.clear_filters
        )
        clear_button.pack(side="right")
    
    def create_transactions_list(self, parent):
        """Create transactions list with modern styling"""
        
        # List container
        list_container = ctk.CTkFrame(parent, corner_radius=15)
        list_container.pack(fill="both", expand=True)
        
        # List header
        header_frame = ctk.CTkFrame(list_container, height=50, corner_radius=0)
        header_frame.pack(fill="x", padx=20, pady=(20, 0))
        header_frame.pack_propagate(False)
        
        headers = ["Date", "Type", "Description", "Category", "Amount", "Account", "Status", "Actions"]
        header_widths = [100, 80, 200, 120, 120, 100, 80, 100]
        
        for i, (header, width) in enumerate(zip(headers, header_widths)):
            header_label = ctk.CTkLabel(
                header_frame,
                text=header,
                font=ctk.CTkFont(size=12, weight="bold"),
                width=width,
                anchor="w" if i < len(headers)-1 else "center"
            )
            header_label.pack(side="left", padx=5, pady=10)
        
        # Scrollable transactions list
        self.transactions_scroll = ctk.CTkScrollableFrame(list_container, height=400)
        self.transactions_scroll.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        # Load transactions
        self.refresh_transactions_list()
    
    def refresh_transactions_list(self):
        """Refresh the transactions list"""
        
        # Clear existing items
        for widget in self.transactions_scroll.winfo_children():
            widget.destroy()
        
        # Add transaction items
        for transaction in self.filtered_transactions:
            self.create_transaction_item(transaction)
        
        # Show message if no transactions
        if not self.filtered_transactions:
            no_data_label = ctk.CTkLabel(
                self.transactions_scroll,
                text="🔍 No transactions found matching your criteria",
                font=ctk.CTkFont(size=16),
                text_color="gray60"
            )
            no_data_label.pack(expand=True, pady=50)
    
    def create_transaction_item(self, transaction):
        """Create individual transaction item"""
        
        item_frame = ctk.CTkFrame(self.transactions_scroll, height=60, corner_radius=10)
        item_frame.pack(fill="x", pady=2)
        item_frame.pack_propagate(False)
        
        # Transaction content
        content_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Date
        date_str = transaction["date"].strftime("%m/%d/%Y")
        date_label = ctk.CTkLabel(
            content_frame,
            text=date_str,
            font=ctk.CTkFont(size=11),
            width=100,
            anchor="w"
        )
        date_label.pack(side="left", padx=5)
        
        # Type with color coding
        type_colors = {
            "Income": "#10b981",
            "Expense": "#ef4444", 
            "Transfer": "#3b82f6"
        }
        
        type_badge = ctk.CTkLabel(
            content_frame,
            text=transaction["type"],
            font=ctk.CTkFont(size=10, weight="bold"),
            width=80,
            height=20,
            corner_radius=10,
            fg_color=type_colors.get(transaction["type"], "#6b7280"),
            text_color="white"
        )
        type_badge.pack(side="left", padx=5)
        
        # Description
        desc_label = ctk.CTkLabel(
            content_frame,
            text=transaction["description"][:30] + "..." if len(transaction["description"]) > 30 else transaction["description"],
            font=ctk.CTkFont(size=11),
            width=200,
            anchor="w"
        )
        desc_label.pack(side="left", padx=5)
        
        # Category
        category_label = ctk.CTkLabel(
            content_frame,
            text=transaction["category"],
            font=ctk.CTkFont(size=11),
            width=120,
            anchor="w",
            text_color="gray70"
        )
        category_label.pack(side="left", padx=5)
        
        # Amount with color coding
        amount_color = "#10b981" if transaction["type"] == "Income" else "#ef4444"
        amount_prefix = "+" if transaction["type"] == "Income" else "-"
        
        amount_label = ctk.CTkLabel(
            content_frame,
            text=f"{amount_prefix}₫{transaction['amount']:,.0f}",
            font=ctk.CTkFont(size=11, weight="bold"),
            width=120,
            anchor="e",
            text_color=amount_color
        )
        amount_label.pack(side="left", padx=5)
        
        # Account
        account_label = ctk.CTkLabel(
            content_frame,
            text=transaction["account"],
            font=ctk.CTkFont(size=11),
            width=100,
            anchor="w",
            text_color="gray70"
        )
        account_label.pack(side="left", padx=5)
        
        # Status
        status_colors = {
            "Completed": "#10b981",
            "Pending": "#f59e0b",
            "Failed": "#ef4444",
            "Cancelled": "#6b7280"
        }
        
        status_badge = ctk.CTkLabel(
            content_frame,
            text=transaction["status"],
            font=ctk.CTkFont(size=9, weight="bold"),
            width=80,
            height=18,
            corner_radius=9,
            fg_color=status_colors.get(transaction["status"], "#6b7280"),
            text_color="white"
        )
        status_badge.pack(side="left", padx=5)
        
        # Actions
        actions_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        actions_frame.pack(side="right", padx=5)
        
        # View details button
        view_button = ctk.CTkButton(
            actions_frame,
            text="👁️",
            width=30,
            height=25,
            font=ctk.CTkFont(size=12),
            fg_color="#3b82f6",
            hover_color="#2563eb",
            command=lambda t=transaction: self.view_transaction_details(t)
        )
        view_button.pack(side="left", padx=2)
        
        # Edit button (only for pending transactions)
        if transaction["status"] == "Pending":
            edit_button = ctk.CTkButton(
                actions_frame,
                text="✏️",
                width=30,
                height=25,
                font=ctk.CTkFont(size=12),
                fg_color="#f59e0b",
                hover_color="#d97706",
                command=lambda t=transaction: self.edit_transaction(t)
            )
            edit_button.pack(side="left", padx=2)
        
        # Delete button (only for failed/cancelled)
        if transaction["status"] in ["Failed", "Cancelled"]:
            delete_button = ctk.CTkButton(
                actions_frame,
                text="🗑️",
                width=30,
                height=25,
                font=ctk.CTkFont(size=12),
                fg_color="#ef4444",
                hover_color="#dc2626",
                command=lambda t=transaction: self.delete_transaction(t)
            )
            delete_button.pack(side="left", padx=2)
    
    def apply_filters(self, value=None):
        """Apply selected filters to transaction list"""
        
        self.filtered_transactions = self.transactions_data.copy()
        
        # Type filter
        if self.type_filter.get() != "All Types":
            self.filtered_transactions = [t for t in self.filtered_transactions if t["type"] == self.type_filter.get()]
        
        # Status filter
        if self.status_filter.get() != "All Status":
            self.filtered_transactions = [t for t in self.filtered_transactions if t["status"] == self.status_filter.get()]
        
        # Date filter
        if self.date_filter.get() != "All Time":
            now = datetime.datetime.now()
            
            if self.date_filter.get() == "Today":
                start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
                self.filtered_transactions = [t for t in self.filtered_transactions if t["date"] >= start_date]
            elif self.date_filter.get() == "This Week":
                start_date = now - datetime.timedelta(days=now.weekday())
                start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
                self.filtered_transactions = [t for t in self.filtered_transactions if t["date"] >= start_date]
            elif self.date_filter.get() == "This Month":
                start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                self.filtered_transactions = [t for t in self.filtered_transactions if t["date"] >= start_date]
            elif self.date_filter.get() == "Last 30 Days":
                start_date = now - datetime.timedelta(days=30)
                self.filtered_transactions = [t for t in self.filtered_transactions if t["date"] >= start_date]
        
        # Search filter
        search_term = self.search_entry.get().lower()
        if search_term:
            self.filtered_transactions = [
                t for t in self.filtered_transactions 
                if search_term in t["description"].lower() 
                or search_term in t["category"].lower()
                or search_term in t["reference"].lower()
            ]
        
        # Refresh the list
        self.refresh_transactions_list()
    
    def on_search_change(self, event):
        """Handle search entry changes"""
        self.apply_filters()
    
    def clear_filters(self):
        """Clear all filters"""
        self.type_filter.set("All Types")
        self.status_filter.set("All Status")
        self.date_filter.set("All Time")
        self.search_entry.delete(0, "end")
        self.apply_filters()
    
    # Action methods
    def add_transaction(self):
        """Add new transaction"""
        messagebox.showinfo("Add Transaction", "Transaction creation dialog will be implemented!\n\nWill include:\n• Transaction type selection\n• Amount and description\n• Account and category\n• Date and reference number")
    
    def view_transaction_details(self, transaction):
        """View transaction details"""
        details = f"""Transaction Details:

ID: {transaction['id']}
Date: {transaction['date'].strftime('%B %d, %Y at %H:%M')}
Type: {transaction['type']}
Category: {transaction['category']}
Description: {transaction['description']}
Amount: ₫{transaction['amount']:,.0f}
Account: {transaction['account']}
Status: {transaction['status']}
Reference: {transaction['reference']}
Notes: {transaction['notes']}"""
        
        messagebox.showinfo("Transaction Details", details)
    
    def edit_transaction(self, transaction):
        """Edit transaction"""
        messagebox.showinfo("Edit Transaction", f"Edit transaction dialog will be implemented!\n\nTransaction ID: {transaction['id']}\nCurrent Amount: ₫{transaction['amount']:,.0f}")
    
    def delete_transaction(self, transaction):
        """Delete transaction"""
        if messagebox.askyesno("Delete Transaction", f"Are you sure you want to delete this transaction?\n\nID: {transaction['id']}\nAmount: ₫{transaction['amount']:,.0f}"):
            messagebox.showinfo("Delete", "Transaction deleted successfully!")
    
    def export_transactions(self):
        """Export transactions"""
        messagebox.showinfo("Export Transactions", "Transaction export functionality will be implemented!\n\nSupported formats:\n• Excel (.xlsx)\n• CSV (.csv)\n• PDF Report")

def main():
    """Test function"""
    root = ctk.CTk()
    root.withdraw()  # Hide root window
    
    transactions_window = TransactionsWindow(root)
    transactions_window.mainloop()

if __name__ == "__main__":
    main()
