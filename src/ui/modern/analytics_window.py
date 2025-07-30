"""
FinanTidy - Analytics Dashboard Module
Modern CustomTkinter interface with charts and financial analytics
"""

import customtkinter as ctk
from tkinter import messagebox
import datetime
import random
import math

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AnalyticsWindow(ctk.CTkToplevel):
    """Modern Analytics Dashboard Window"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Window configuration
        self.title("FinanTidy - Analytics Dashboard")
        self.geometry("1500x900")
        self.transient(parent)
        
        # Generate sample analytics data
        self.analytics_data = self.generate_sample_data()
        
        # Create UI
        self.create_analytics_ui()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (1500 // 2)
        y = (self.winfo_screenheight() // 2) - (900 // 2)
        self.geometry(f"1500x900+{x}+{y}")
    
    def generate_sample_data(self):
        """Generate sample analytics data"""
        
        # Monthly revenue data
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthly_revenue = [random.randint(80000000, 150000000) for _ in range(12)]
        
        # Provider breakdown
        provider_data = [
            {"name": "Tech Solutions", "amount": 45000000, "percentage": 30},
            {"name": "Marketing Pro", "amount": 35000000, "percentage": 23},
            {"name": "Office Supplies", "amount": 25000000, "percentage": 17},
            {"name": "Legal Advisory", "amount": 20000000, "percentage": 13},
            {"name": "Others", "amount": 25000000, "percentage": 17}
        ]
        
        # Invoice status data
        invoice_status = {
            "Paid": {"count": 156, "amount": 89000000, "color": "#10b981"},
            "Pending": {"count": 28, "amount": 32000000, "color": "#f59e0b"},
            "Overdue": {"count": 12, "amount": 18000000, "color": "#ef4444"},
            "Draft": {"count": 8, "amount": 11000000, "color": "#6b7280"}
        }
        
        # Growth metrics
        growth_metrics = {
            "revenue_growth": 12.5,
            "invoice_growth": 8.3,
            "provider_growth": 15.7,
            "profit_margin": 23.4
        }
        
        return {
            "monthly_revenue": monthly_revenue,
            "months": months,
            "provider_data": provider_data,
            "invoice_status": invoice_status,
            "growth_metrics": growth_metrics
        }
    
    def create_analytics_ui(self):
        """Create analytics dashboard interface"""
        
        # Main container
        main_container = ctk.CTkFrame(self, corner_radius=0)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Scrollable content
        self.scroll_frame = ctk.CTkScrollableFrame(main_container)
        self.scroll_frame.pack(fill="both", expand=True, pady=(20, 0))
        
        # Create dashboard sections
        self.create_overview_section()
        self.create_charts_section()
        self.create_insights_section()
    
    def create_header(self, parent):
        """Create header with title and controls"""
        
        header_frame = ctk.CTkFrame(parent, height=80, corner_radius=15)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Left side - Title
        left_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="y", padx=25, pady=20)
        
        title_label = ctk.CTkLabel(
            left_frame,
            text="📈 Analytics Dashboard",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(anchor="w")
        
        subtitle_label = ctk.CTkLabel(
            left_frame,
            text="Financial insights and performance metrics",
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        subtitle_label.pack(anchor="w")
        
        # Right side - Controls
        right_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="y", padx=25, pady=20)
        
        # Time period selector
        time_period = ctk.CTkOptionMenu(
            right_frame,
            values=["Last 30 Days", "Last 3 Months", "Last 6 Months", "This Year", "All Time"],
            width=150,
            height=35
        )
        time_period.pack(side="right", padx=(10, 0))
        time_period.set("This Year")
        
        # Refresh button
        refresh_button = ctk.CTkButton(
            right_frame,
            text="🔄 Refresh",
            height=35,
            width=100,
            font=ctk.CTkFont(size=14),
            command=self.refresh_data
        )
        refresh_button.pack(side="right", padx=(10, 0))
        
        # Export button
        export_button = ctk.CTkButton(
            right_frame,
            text="📊 Export",
            height=35,
            width=100,
            font=ctk.CTkFont(size=14),
            fg_color="#10b981",
            hover_color="#059669",
            command=self.export_analytics
        )
        export_button.pack(side="right")
    
    def create_overview_section(self):
        """Create overview metrics section"""
        
        # Section title
        section_title = ctk.CTkLabel(
            self.scroll_frame,
            text="📊 Performance Overview",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        section_title.pack(anchor="w", padx=20, pady=(20, 15))
        
        # Metrics container
        metrics_container = ctk.CTkFrame(self.scroll_frame, corner_radius=15)
        metrics_container.pack(fill="x", padx=20, pady=(0, 20))
        
        # Configure grid
        metrics_container.grid_columnconfigure(0, weight=1)
        metrics_container.grid_columnconfigure(1, weight=1)
        metrics_container.grid_columnconfigure(2, weight=1)
        metrics_container.grid_columnconfigure(3, weight=1)
        
        # Metrics data
        metrics = [
            ("💰", "Total Revenue", "₫150.2M", f"+{self.analytics_data['growth_metrics']['revenue_growth']}%", "#10b981"),
            ("📄", "Total Invoices", "204", f"+{self.analytics_data['growth_metrics']['invoice_growth']}%", "#3b82f6"),
            ("🏪", "Active Providers", "15", f"+{self.analytics_data['growth_metrics']['provider_growth']}%", "#f59e0b"),
            ("📈", "Profit Margin", f"{self.analytics_data['growth_metrics']['profit_margin']}%", "+2.1%", "#8b5cf6")
        ]
        
        for i, (icon, title, value, change, color) in enumerate(metrics):
            metric_card = self.create_metric_card(metrics_container, icon, title, value, change, color)
            metric_card.grid(row=0, column=i, padx=15, pady=20, sticky="ew")
    
    def create_metric_card(self, parent, icon, title, value, change, color):
        """Create individual metric card"""
        
        card = ctk.CTkFrame(parent, corner_radius=12, height=120)
        card.pack_propagate(False)
        
        # Content
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Icon container
        icon_frame = ctk.CTkFrame(content, fg_color="transparent")
        icon_frame.pack(fill="x")
        
        icon_container = ctk.CTkFrame(icon_frame, width=50, height=50, corner_radius=25, fg_color=color)
        icon_container.pack(side="left")
        icon_container.pack_propagate(False)
        
        icon_label = ctk.CTkLabel(
            icon_container,
            text=icon,
            font=ctk.CTkFont(size=24)
        )
        icon_label.pack(expand=True)
        
        # Change indicator
        change_label = ctk.CTkLabel(
            icon_frame,
            text=change,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#10b981" if change.startswith("+") else "#ef4444"
        )
        change_label.pack(side="right")
        
        # Value
        value_label = ctk.CTkLabel(
            content,
            text=value,
            font=ctk.CTkFont(size=24, weight="bold")
        )
        value_label.pack(anchor="w", pady=(10, 0))
        
        # Title
        title_label = ctk.CTkLabel(
            content,
            text=title,
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        title_label.pack(anchor="w")
        
        return card
    
    def create_charts_section(self):
        """Create charts section"""
        
        # Section title
        section_title = ctk.CTkLabel(
            self.scroll_frame,
            text="📈 Financial Charts",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        section_title.pack(anchor="w", padx=20, pady=(20, 15))
        
        # Charts container
        charts_container = ctk.CTkFrame(self.scroll_frame, corner_radius=15)
        charts_container.pack(fill="x", padx=20, pady=(0, 20))
        
        # Configure grid
        charts_container.grid_columnconfigure(0, weight=2)
        charts_container.grid_columnconfigure(1, weight=1)
        charts_container.grid_rowconfigure(0, weight=1)
        
        # Revenue chart (left)
        self.create_revenue_chart(charts_container)
        
        # Provider breakdown (right)
        self.create_provider_breakdown(charts_container)
    
    def create_revenue_chart(self, parent):
        """Create revenue trend chart (simulated)"""
        
        chart_frame = ctk.CTkFrame(parent, corner_radius=12)
        chart_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")
        
        # Chart title
        title = ctk.CTkLabel(
            chart_frame,
            text="📊 Monthly Revenue Trend",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title.pack(pady=(20, 15))
        
        # Chart area (simulated with bars)
        chart_area = ctk.CTkFrame(chart_frame, height=300, corner_radius=8)
        chart_area.pack(fill="x", padx=20, pady=(0, 20))
        chart_area.pack_propagate(False)
        
        # Simulated bar chart
        bars_frame = ctk.CTkFrame(chart_area, fg_color="transparent")
        bars_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Create bars for each month
        max_revenue = max(self.analytics_data["monthly_revenue"])
        months = self.analytics_data["months"][:6]  # Show last 6 months
        revenues = self.analytics_data["monthly_revenue"][:6]
        
        for i, (month, revenue) in enumerate(zip(months, revenues)):
            # Bar container
            bar_container = ctk.CTkFrame(bars_frame, fg_color="transparent")
            bar_container.pack(side="left", fill="both", expand=True, padx=2)
            
            # Calculate bar height (proportional)
            bar_height = int((revenue / max_revenue) * 200)
            
            # Spacer to push bar to bottom
            spacer = ctk.CTkFrame(bar_container, fg_color="transparent", height=200-bar_height)
            spacer.pack(fill="x")
            
            # Bar
            bar = ctk.CTkFrame(bar_container, height=bar_height, corner_radius=4, fg_color="#1f538d")
            bar.pack(fill="x")
            
            # Month label
            month_label = ctk.CTkLabel(
                bar_container,
                text=month,
                font=ctk.CTkFont(size=10),
                text_color="gray70"
            )
            month_label.pack(pady=(5, 0))
            
            # Value label
            value_label = ctk.CTkLabel(
                bar_container,
                text=f"₫{revenue//1000000}M",
                font=ctk.CTkFont(size=9, weight="bold")
            )
            value_label.pack()
    
    def create_provider_breakdown(self, parent):
        """Create provider breakdown chart (simulated pie chart)"""
        
        breakdown_frame = ctk.CTkFrame(parent, corner_radius=12)
        breakdown_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew")
        
        # Chart title
        title = ctk.CTkLabel(
            breakdown_frame,
            text="🏪 Provider Breakdown",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title.pack(pady=(20, 15))
        
        # Pie chart simulation (using colored circles)
        pie_area = ctk.CTkFrame(breakdown_frame, height=200, corner_radius=8)
        pie_area.pack(fill="x", padx=20, pady=(0, 10))
        pie_area.pack_propagate(False)
        
        # Center message
        center_label = ctk.CTkLabel(
            pie_area,
            text="📊\nProvider\nDistribution",
            font=ctk.CTkFont(size=16, weight="bold"),
            justify="center"
        )
        center_label.pack(expand=True)
        
        # Legend
        legend_frame = ctk.CTkFrame(breakdown_frame, fg_color="transparent")
        legend_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        colors = ["#1f538d", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6"]
        
        for i, provider in enumerate(self.analytics_data["provider_data"]):
            legend_item = ctk.CTkFrame(legend_frame, fg_color="transparent")
            legend_item.pack(fill="x", pady=2)
            
            # Color indicator
            color_dot = ctk.CTkFrame(
                legend_item, 
                width=15, 
                height=15, 
                corner_radius=7, 
                fg_color=colors[i % len(colors)]
            )
            color_dot.pack(side="left", padx=(0, 10))
            color_dot.pack_propagate(False)
            
            # Provider info
            info_label = ctk.CTkLabel(
                legend_item,
                text=f"{provider['name']} ({provider['percentage']}%)",
                font=ctk.CTkFont(size=12),
                anchor="w"
            )
            info_label.pack(side="left", fill="x", expand=True)
            
            # Amount
            amount_label = ctk.CTkLabel(
                legend_item,
                text=f"₫{provider['amount']//1000000}M",
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color="gray70"
            )
            amount_label.pack(side="right")
    
    def create_insights_section(self):
        """Create insights and recommendations section"""
        
        # Section title
        section_title = ctk.CTkLabel(
            self.scroll_frame,
            text="💡 Business Insights",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        section_title.pack(anchor="w", padx=20, pady=(20, 15))
        
        # Insights container
        insights_container = ctk.CTkFrame(self.scroll_frame, corner_radius=15)
        insights_container.pack(fill="x", padx=20, pady=(0, 20))
        
        # Configure grid
        insights_container.grid_columnconfigure(0, weight=1)
        insights_container.grid_columnconfigure(1, weight=1)
        
        # Invoice status analysis (left)
        self.create_invoice_status_analysis(insights_container)
        
        # Recommendations (right)
        self.create_recommendations(insights_container)
    
    def create_invoice_status_analysis(self, parent):
        """Create invoice status analysis"""
        
        status_frame = ctk.CTkFrame(parent, corner_radius=12)
        status_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")
        
        # Title
        title = ctk.CTkLabel(
            status_frame,
            text="📄 Invoice Status Analysis",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title.pack(pady=(20, 15))
        
        # Status items
        for status, data in self.analytics_data["invoice_status"].items():
            status_item = ctk.CTkFrame(status_frame, height=60, corner_radius=8)
            status_item.pack(fill="x", padx=20, pady=5)
            status_item.pack_propagate(False)
            
            content = ctk.CTkFrame(status_item, fg_color="transparent")
            content.pack(fill="both", expand=True, padx=15, pady=10)
            
            # Status indicator
            indicator = ctk.CTkFrame(
                content,
                width=30,
                height=30,
                corner_radius=15,
                fg_color=data["color"]
            )
            indicator.pack(side="left")
            indicator.pack_propagate(False)
            
            # Status info
            info_frame = ctk.CTkFrame(content, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, padx=(15, 0))
            
            status_label = ctk.CTkLabel(
                info_frame,
                text=status,
                font=ctk.CTkFont(size=14, weight="bold"),
                anchor="w"
            )
            status_label.pack(fill="x")
            
            details_label = ctk.CTkLabel(
                info_frame,
                text=f"{data['count']} invoices • ₫{data['amount']//1000000}M",
                font=ctk.CTkFont(size=12),
                text_color="gray70",
                anchor="w"
            )
            details_label.pack(fill="x")
            
            # Percentage
            total_amount = sum(d['amount'] for d in self.analytics_data["invoice_status"].values())
            percentage = (data['amount'] / total_amount) * 100
            
            percentage_label = ctk.CTkLabel(
                content,
                text=f"{percentage:.1f}%",
                font=ctk.CTkFont(size=16, weight="bold")
            )
            percentage_label.pack(side="right")
        
        # Add spacing at bottom
        ctk.CTkFrame(status_frame, height=20, fg_color="transparent").pack()
    
    def create_recommendations(self, parent):
        """Create business recommendations"""
        
        recommendations_frame = ctk.CTkFrame(parent, corner_radius=12)
        recommendations_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew")
        
        # Title
        title = ctk.CTkLabel(
            recommendations_frame,
            text="🎯 Recommendations",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title.pack(pady=(20, 15))
        
        # Recommendations list
        recommendations = [
            {
                "icon": "⚠️",
                "title": "Overdue Invoices",
                "description": "12 invoices are overdue. Follow up to improve cash flow.",
                "priority": "High",
                "color": "#ef4444"
            },
            {
                "icon": "📈",
                "title": "Growth Opportunity",
                "description": "Revenue increased 12.5% this month. Consider expanding services.",
                "priority": "Medium",
                "color": "#10b981"
            },
            {
                "icon": "🏪",
                "title": "Provider Diversification",
                "description": "Top 3 providers account for 70% of expenses. Consider diversifying.",
                "priority": "Medium",
                "color": "#f59e0b"
            },
            {
                "icon": "💰",
                "title": "Profit Optimization",
                "description": "Profit margin at 23.4%. Review pricing strategy for improvement.",
                "priority": "Low",
                "color": "#8b5cf6"
            }
        ]
        
        for rec in recommendations:
            rec_item = ctk.CTkFrame(recommendations_frame, corner_radius=8)
            rec_item.pack(fill="x", padx=20, pady=5)
            
            content = ctk.CTkFrame(rec_item, fg_color="transparent")
            content.pack(fill="both", expand=True, padx=15, pady=12)
            
            # Header
            header = ctk.CTkFrame(content, fg_color="transparent")
            header.pack(fill="x")
            
            # Icon and title
            icon_title = ctk.CTkFrame(header, fg_color="transparent")
            icon_title.pack(side="left", fill="x", expand=True)
            
            title_label = ctk.CTkLabel(
                icon_title,
                text=f"{rec['icon']} {rec['title']}",
                font=ctk.CTkFont(size=13, weight="bold"),
                anchor="w"
            )
            title_label.pack(anchor="w")
            
            # Priority badge
            priority_colors = {
                "High": "#ef4444",
                "Medium": "#f59e0b", 
                "Low": "#6b7280"
            }
            
            priority_badge = ctk.CTkLabel(
                header,
                text=rec["priority"],
                font=ctk.CTkFont(size=10, weight="bold"),
                text_color="white",
                corner_radius=6,
                fg_color=priority_colors[rec["priority"]],
                width=50,
                height=18
            )
            priority_badge.pack(side="right")
            
            # Description
            desc_label = ctk.CTkLabel(
                content,
                text=rec["description"],
                font=ctk.CTkFont(size=11),
                text_color="gray70",
                anchor="w",
                justify="left",
                wraplength=300
            )
            desc_label.pack(anchor="w", pady=(5, 0))
        
        # Add spacing at bottom
        ctk.CTkFrame(recommendations_frame, height=20, fg_color="transparent").pack()
    
    def refresh_data(self):
        """Refresh analytics data"""
        # Regenerate sample data
        self.analytics_data = self.generate_sample_data()
        
        # Clear and recreate all sections
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
        
        self.create_overview_section()
        self.create_charts_section()
        self.create_insights_section()
        
        messagebox.showinfo("Refresh", "Analytics data refreshed successfully!")
    
    def export_analytics(self):
        """Export analytics report"""
        messagebox.showinfo("Export Analytics", "Analytics export functionality will be implemented next!\n\nWill support PDF, Excel, and CSV formats.")

def main():
    """Test function"""
    root = ctk.CTk()
    root.withdraw()  # Hide root window
    
    analytics_window = AnalyticsWindow(root)
    analytics_window.mainloop()

if __name__ == "__main__":
    main()
