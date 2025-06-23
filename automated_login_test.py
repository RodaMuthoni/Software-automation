"""
Automated Login Testing with AI-Enhanced Selenium
=================================================
This script demonstrates automated testing of login functionality using Selenium WebDriver
with AI-enhanced test case generation and result analysis.

Author: AI Software Engineering Assignment
Task: Week 4 - Task 2: Automated Testing with AI
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json
from datetime import datetime

class AILoginTester:
    """
    AI-Enhanced Login Testing Class
    Automates login testing with intelligent test case generation and result analysis
    """
    
    def __init__(self, base_url="https://the-internet.herokuapp.com/login"):
        """Initialize the tester with configuration"""
        self.base_url = base_url
        self.driver = None
        self.test_results = []
        self.setup_driver()
    
    def setup_driver(self):
        """Setup Chrome WebDriver with optimized options"""
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(10)
            print("✅ WebDriver initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize WebDriver: {e}")
    
    def generate_test_cases(self):
        """
        AI-Enhanced Test Case Generation
        Returns intelligent test cases covering various scenarios
        """
        return [
            # Valid credentials
            {
                "name": "Valid Login - Correct Credentials",
                "username": "tomsmith",
                "password": "SuperSecretPassword!",
                "expected_result": "success",
                "description": "Test successful login with valid credentials"
            },
            # Invalid username scenarios
            {
                "name": "Invalid Login - Wrong Username",
                "username": "wronguser",
                "password": "SuperSecretPassword!",
                "expected_result": "failure",
                "description": "Test login failure with incorrect username"
            },
            # Invalid password scenarios
            {
                "name": "Invalid Login - Wrong Password",
                "username": "tomsmith",
                "password": "wrongpassword",
                "expected_result": "failure",
                "description": "Test login failure with incorrect password"
            },
            # Edge cases
            {
                "name": "Invalid Login - Empty Credentials",
                "username": "",
                "password": "",
                "expected_result": "failure",
                "description": "Test login failure with empty credentials"
            },
            {
                "name": "Invalid Login - SQL Injection Attempt",
                "username": "admin' OR '1'='1",
                "password": "password",
                "expected_result": "failure",
                "description": "Test security against SQL injection"
            },
            {
                "name": "Invalid Login - Special Characters",
                "username": "user@#$%",
                "password": "pass@#$%",
                "expected_result": "failure",
                "description": "Test handling of special characters"
            }
        ]
    
    def execute_login_test(self, test_case):
        """
        Execute individual login test case
        Returns detailed test result with AI analysis
        """
        start_time = time.time()
        result = {
            "test_name": test_case["name"],
            "description": test_case["description"],
            "username": test_case["username"],
            "password": test_case["password"],
            "expected_result": test_case["expected_result"],
            "actual_result": None,
            "status": "FAIL",
            "execution_time": 0,
            "error_message": None,
            "screenshot_taken": False,
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            # Navigate to login page
            self.driver.get(self.base_url)
            print(f"🔄 Executing: {test_case['name']}")
            
            # Find and fill username field
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(test_case["username"])
            
            # Find and fill password field
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(test_case["password"])
            
            # Click login button
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Wait for page response and analyze result
            time.sleep(2)
            
            # Check for success indicators
            success_indicators = [
                (By.CSS_SELECTOR, ".flash.success"),
                (By.PARTIAL_LINK_TEXT, "Logout"),
                (By.CSS_SELECTOR, "[href='/logout']")
            ]
            
            # Check for failure indicators
            failure_indicators = [
                (By.CSS_SELECTOR, ".flash.error"),
                (By.XPATH, "//*[contains(text(), 'invalid')]"),
                (By.XPATH, "//*[contains(text(), 'Your username is invalid')]")
            ]
            
            # Determine actual result using AI logic
            login_successful = False
            error_found = False
            
            for locator in success_indicators:
                try:
                    element = self.driver.find_element(*locator)
                    if element and element.is_displayed():
                        login_successful = True
                        break
                except NoSuchElementException:
                    continue
            
            for locator in failure_indicators:
                try:
                    element = self.driver.find_element(*locator)
                    if element and element.is_displayed():
                        error_found = True
                        result["error_message"] = element.text
                        break
                except NoSuchElementException:
                    continue
            
            # Determine test result
            if login_successful:
                result["actual_result"] = "success"
            elif error_found:
                result["actual_result"] = "failure"
            else:
                result["actual_result"] = "unknown"
            
            # Validate against expected result
            if result["actual_result"] == test_case["expected_result"]:
                result["status"] = "PASS"
                print(f"✅ PASSED: {test_case['name']}")
            else:
                result["status"] = "FAIL"
                print(f"❌ FAILED: {test_case['name']}")
                print(f"   Expected: {test_case['expected_result']}, Got: {result['actual_result']}")
            
        except Exception as e:
            result["status"] = "ERROR"
            result["error_message"] = str(e)
            print(f"💥 ERROR in {test_case['name']}: {e}")
        
        finally:
            result["execution_time"] = round(time.time() - start_time, 2)
        
        return result
    
    def run_ai_test_suite(self):
        """
        Execute complete AI-enhanced test suite
        Returns comprehensive test results with analytics
        """
        print("\n🚀 Starting AI-Enhanced Login Test Suite")
        print("=" * 50)
        
        test_cases = self.generate_test_cases()
        suite_start_time = time.time()
        
        for test_case in test_cases:
            result = self.execute_login_test(test_case)
            self.test_results.append(result)
            time.sleep(1)  # Brief pause between tests
        
        total_execution_time = round(time.time() - suite_start_time, 2)
        
        # Generate AI analytics
        analytics = self.generate_ai_analytics(total_execution_time)
        
        return {
            "results": self.test_results,
            "analytics": analytics,
            "total_execution_time": total_execution_time
        }
    
    def generate_ai_analytics(self, total_time):
        """
        AI-powered test result analysis and insights
        """
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results if r["status"] == "PASS"])
        failed_tests = len([r for r in self.test_results if r["status"] == "FAIL"])
        error_tests = len([r for r in self.test_results if r["status"] == "ERROR"])
        
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        avg_execution_time = sum([r["execution_time"] for r in self.test_results]) / total_tests
        
        # AI insights
        insights = []
        
        if success_rate == 100:
            insights.append("🎯 Perfect test execution - all scenarios handled correctly")
        elif success_rate >= 80:
            insights.append("✅ Good test coverage with high success rate")
        else:
            insights.append("⚠️ Some test scenarios may need attention")
        
        if avg_execution_time < 3:
            insights.append("⚡ Fast execution times indicate efficient test design")
        elif avg_execution_time > 5:
            insights.append("🐌 Consider optimizing test execution speed")
        
        # Security analysis
        security_tests = [r for r in self.test_results if "injection" in r["test_name"].lower() or "special" in r["test_name"].lower()]
        if security_tests and all(r["status"] == "PASS" for r in security_tests):
            insights.append("🔒 Security tests passed - application shows good input validation")
        
        return {
            "total_tests": total_tests,
            "passed": passed_tests,
            "failed": failed_tests,
            "errors": error_tests,
            "success_rate": round(success_rate, 2),
            "avg_execution_time": round(avg_execution_time, 2),
            "total_time": total_time,
            "insights": insights,
            "test_coverage_areas": [
                "Authentication validation",
                "Input sanitization",
                "Error handling",
                "Security testing",
                "Edge case handling"
            ]
        }
    
    def generate_report(self, results):
        """Generate comprehensive test report"""
        print("\n" + "=" * 60)
        print("🤖 AI-ENHANCED LOGIN TESTING REPORT")
        print("=" * 60)
        
        analytics = results["analytics"]
        
        print(f"\n📊 TEST EXECUTION SUMMARY:")
        print(f"   Total Tests: {analytics['total_tests']}")
        print(f"   Passed: {analytics['passed']} ✅")
        print(f"   Failed: {analytics['failed']} ❌")
        print(f"   Errors: {analytics['errors']} 💥")
        print(f"   Success Rate: {analytics['success_rate']}%")
        print(f"   Total Execution Time: {analytics['total_time']}s")
        print(f"   Average Test Time: {analytics['avg_execution_time']}s")
        
        print(f"\n🧠 AI INSIGHTS:")
        for insight in analytics['insights']:
            print(f"   {insight}")
        
        print(f"\n🎯 TEST COVERAGE AREAS:")
        for area in analytics['test_coverage_areas']:
            print(f"   • {area}")
        
        print(f"\n📋 DETAILED TEST RESULTS:")
        for result in results["results"]:
            status_icon = "✅" if result["status"] == "PASS" else "❌" if result["status"] == "FAIL" else "💥"
            print(f"\n   {status_icon} {result['test_name']}")
            print(f"      Expected: {result['expected_result']} | Actual: {result['actual_result']}")
            print(f"      Time: {result['execution_time']}s")
            if result['error_message']:
                print(f"      Error: {result['error_message']}")
        
        print("\n" + "=" * 60)
    
    def save_results_json(self, results, filename="ai_login_test_results.json"):
        """Save test results to JSON file for further analysis"""
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            print(f"💾 Results saved to {filename}")
        except Exception as e:
            print(f"❌ Failed to save results: {e}")
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            self.driver.quit()
            print("🧹 WebDriver cleaned up successfully")
    

    def generate_html_report(self, results, filename="ai_login_report.html"):
        """Generate an HTML report with styled visual results"""
        analytics = results["analytics"]
        tests = results["results"]

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>AI Login Test Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 20px; background: #f7f9fc; color: #333; }}
                h1 {{ color: #2c3e50; }}
                .summary, .insights, .test-results {{ margin-bottom: 30px; }}
                .passed {{ color: green; }}
                .failed, .error {{ color: red; }}
                .box {{ background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background-color: #e9eef3; }}
            </style>
        </head>
        <body>
            <h1>🤖 AI-Enhanced Login Testing Report</h1>
            
            <div class="summary box">
                <h2>📊 Summary</h2>
                <p>Total Tests: <strong>{analytics['total_tests']}</strong></p>
                <p>✅ Passed: <strong>{analytics['passed']}</strong></p>
                <p>❌ Failed: <strong>{analytics['failed']}</strong></p>
                <p>💥 Errors: <strong>{analytics['errors']}</strong></p>
                <p>🎯 Success Rate: <strong>{analytics['success_rate']}%</strong></p>
                <p>⏱ Average Test Time: <strong>{analytics['avg_execution_time']}s</strong></p>
            </div>

            <div class="insights box">
                <h2>🧠 AI Insights</h2>
                <ul>
                    {''.join(f"<li>{insight}</li>" for insight in analytics['insights'])}
                </ul>
            </div>

            <div class="test-results box">
                <h2>📋 Test Details</h2>
                <table>
                    <tr>
                        <th>Test Name</th>
                        <th>Expected</th>
                        <th>Actual</th>
                        <th>Status</th>
                        <th>Time</th>
                        <th>Error</th>
                    </tr>
        """

        for test in tests:
            status_class = "passed" if test["status"] == "PASS" else "failed" if test["status"] == "FAIL" else "error"
            html += f"""
                <tr class="{status_class}">
                    <td>{test['test_name']}</td>
                    <td>{test['expected_result']}</td>
                    <td>{test['actual_result']}</td>
                    <td class="{status_class}">{test['status']}</td>
                    <td>{test['execution_time']}s</td>
                    <td>{test['error_message'] or '-'}</td>
                </tr>
            """

        html += """
                </table>
            </div>
        </body>
        </html>
        """

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"🌐 HTML report generated: {filename}")
        except Exception as e:
            print(f"❌ Failed to generate HTML report: {e}")


def main():
    """
    Main execution function for AI-Enhanced Login Testing
    """
    tester = None
    try:
        # Initialize AI Login Tester
        tester = AILoginTester()
        
        # Run comprehensive test suite
        results = tester.run_ai_test_suite()
        
        # Generate and display report
        tester.generate_report(results)
        
        # Save results for analysis
        tester.save_results_json(results)

        tester.generate_html_report(results)
        
        print("\n🎉 AI-Enhanced Login Testing Complete!")
        
        return results
        
    except Exception as e:
        print(f"💥 Critical error in test execution: {e}")
        return None
    
    finally:
        if tester:
            tester.cleanup()

if __name__ == "__main__":
    # Execute the AI-enhanced testing suite
    test_results = main()
    
    # Display success message
    if test_results:
        success_rate = test_results["analytics"]["success_rate"]
        print(f"\n🎯 Final Success Rate: {success_rate}%")
        print("📈 AI has successfully automated and analyzed login testing!")




































































