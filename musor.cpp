#include <iostream>
#include <string>
#include <fstream>

struct book
    {
        std::string code;
        std::string name;
        std::string autor;
        std::string year;
        std::string count;
        std::string edition;
    };

struct node
    {
        node * prev{nullptr};
        book data;
        node * next{nullptr};
    };
struct funcbox
    {
        node * head{nullptr};
        node * head2{nullptr};
        node * last{nullptr};
        node * last2{nullptr};
        void roff(std::string filename);
        void add(node * fmp);
        void erase();
        void insert(int n, node * fmp);
        void seelast();
        void size();
        void listcut(int number);
        void compound();
        void write();
    };

int main()
    {
        funcbox s;
        s.roff("lab9.txt");
        node * fmp = new node; fmp->data.code = "0";
        s.add(fmp);
        s.erase();
        s.insert(2,fmp);
        s.seelast();
        //s.size();
        s.listcut(3);
        s.compound();
        s.write();
    }
void funcbox::roff(std::string filename)
    {
        std::ifstream unlock;
        unlock.open(filename);
        std::string temporary; 
        node * tmp = new node;      
        node * obm = new node;
        while (true)
            {
                if (temporary.length() != 0)
                {
                tmp->next = new node;
                int count = 0, words = -1; std::string k = "";
                for (int l = 0; l < temporary.length(); l++)
                    {
                        if (count == 2)
                        {
                            count = 0;
                            k = "";
                        }
                        if (temporary[l] == '"')
                        {
                            count++;
                        }
                        if (count == 1 and temporary[l] != '"')
                        {
                            k = k + temporary[l];
                        }
                        if (count == 2)
                        {
                            words++;
                            switch (words)
                            {
                            case 0:
                            tmp->data.code = k;
                            break;
                            case 1:
                            tmp->data.autor = k;
                            break;
                            case 2:
                            tmp->data.name = k;
                            break;
                            case 3:
                            tmp->data.year = k;
                            break;
                            case 4:
                            tmp->data.count = k;
                            break;
                            case 5:
                                tmp->data.edition = k;
                            break;
                            default:
                            break;
                            }
                        }
                    }
                if (not getline(unlock,temporary))
                    {
                        tmp->next = nullptr;
                        last->next = nullptr;
                        return;
                    }
                
                if (!head)
                        head = tmp;
                else
                    {
                        last = tmp;
                        tmp->prev = obm->prev;
                    }
                obm->prev = tmp;
                tmp = tmp->next;
                }
                else
                    getline(unlock,temporary);
        }
    unlock.close();
    }

void funcbox::add(node * fmp)
    {
        last->next = fmp;
        fmp->prev = last;
        last = fmp;
        last->next =nullptr;
    }

void funcbox::erase()
    {
        node * tmp = head;
        head = head->next;
        head->prev = nullptr;
        delete tmp;
        tmp->next = nullptr;
    }

void funcbox::insert(int n, node * fmp)
    {   
        int i = 1;
        for (node * tmp = head; tmp; tmp = tmp->next)
            {
                if (i == n)
                    {
                        fmp->next = tmp->next;
                        fmp->prev = tmp;
                        tmp->next = fmp;
                        break;
                    }
                i++;
            }
    }

void funcbox::seelast()
    {
        std::cout << last << std::endl;
    }

void funcbox::size()
    {
        int i = 0;
        for (node * tmp = head; tmp; tmp = tmp->next)
            {
                i++;
            }
        std::cout << "size of list: " << i << std::endl;
    }

void funcbox::listcut(int number)
    {
        int i = 1;
        for (node * tmp = head; tmp; tmp = tmp->next)
            {
                if (number == i)
                    {
                        tmp->prev->next = nullptr;
                        last2 = last;
                        last = tmp->prev;
                        tmp->prev = nullptr;
                        head2 = tmp;
                        break;
                    }
                i++;
            }
    }

void funcbox::compound()
    {
        last->next = head2;
        head2->prev = last;
        last = last2;
        last2 = nullptr;
        head2 = nullptr;
    }

void funcbox::write()
    {
        std::ofstream oFile("new file.txt");
        std::ofstream out;
        out.open("new file.txt");
            for (node * tmp = head; tmp ; tmp = tmp->next)
                {
                    out << tmp->data.code << " " << tmp->data.autor << " " << tmp->data.name << " " << tmp->data.year << " " << tmp->data.count << " " << tmp->data.edition << std::endl;
                }
        std::cout << "Yes";
        out.close();
    }