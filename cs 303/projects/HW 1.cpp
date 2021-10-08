#include <iostream>
#include <string>
#include <list>
#include <iterator>
using namespace std;

struct dueDate {
    int month, day, year;
    // override the == operator
    friend bool operator==(dueDate a, dueDate b) {
        if (a.month=b.month && a.day==b.day && a.year==b.year) {
            return true;
        }
        else {
            return false;
        }
    }
};

class Assignment
{
private:
    string assignment_name;
    dueDate due_date; 
public:
    Assignment(string assignment_name, dueDate due_date);
    dueDate get_due_date();
    string get_name();
    ~Assignment();
};

Assignment::Assignment(string assignment_name, dueDate due_date)
{
    this->assignment_name = assignment_name;
    this->due_date = due_date;
}

dueDate Assignment::get_due_date()
{
    return this->due_date;
}

string Assignment::get_name()
{
    return this->assignment_name;
}

Assignment::~Assignment()
{
}

list <Assignment> assignments;

void add_assignment(string assignment_name, dueDate due_date)
{
    Assignment assignment(assignment_name, due_date);
    assignments.push_back(assignment);
}

void del_assignment(string assignment_name, list <Assignment> &a)
{
    list <Assignment> :: iterator it;
    for(it = a.begin(); it != a.end(); it++)
    {
        if (it->get_name() == assignment_name)
        {
            it = a.erase(it);
        }
    }
}

void list_assignments(list <Assignment> a)
{
    list <Assignment> :: iterator it;
    for (it = a.begin(); it != a.end(); it++)
    {
        cout << it->get_name() << "\t";
    }
    cout << endl;
}

dueDate next_due(list<Assignment> loA)
{
    dueDate temp;
    int mon = loA.front().get_due_date().month;
    for (auto f = loA.begin(); f != loA.end(); f++) {
        if (mon > f->get_due_date().month)
            mon = f->get_due_date().month;
    }
    list<Assignment> DDt;
    for (auto f = loA.begin(); f != loA.end(); f++) {
        if (mon == f->get_due_date().month)
            DDt.push_back(*f); 
    }
    auto f = DDt.begin();
    temp = f->get_due_date();
    f++;
    for (;f!=DDt.end();f++) {
        if (f->get_due_date().day < temp.day)
            temp = f->get_due_date();
    }
    return temp;
}

int main()
{
    dueDate date;
    date.day = 15;
    date.month = 9;
    date.year = 2021;

    add_assignment("HW 1", date);
    date.day = 29;
    add_assignment("HW 2", date);
    date.day = 1;
    add_assignment("HW 3", date);
    date.day = 8; date.month = 8; 
    add_assignment("HW 4", date);

    list_assignments(assignments);
    dueDate due_date = next_due(assignments);
    int day = due_date.day, month = due_date.month, year = due_date.year;


    cout << day << ", " << month << ", " << year << endl;

    del_assignment("HW 3", assignments);

    list_assignments(assignments);

    return 0;
}