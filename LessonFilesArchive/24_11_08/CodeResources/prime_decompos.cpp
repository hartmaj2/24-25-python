#include <iostream>
#include <vector>
#include <chrono>

void print_decompos(const std::vector<unsigned long>& decompos)
{
    std::vector<unsigned long>::const_iterator it = decompos.begin();
    std::cout << "[";
    for (auto it = decompos.begin(); it != decompos.end(); ++it)
    {
        std::cout << *it;
        if (it != decompos.end() - 1)
        {
             std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}

int main()
{
    unsigned long number;
    std::cout << "Enter a number to decompose: ";
    std::cin >> number;

    std::vector<unsigned long> decompos;

    unsigned long divisor = 2;

    auto start = std::chrono::system_clock::now();

    while (number != 1)
    {
        if (number % divisor == 0)
        {
            decompos.push_back(divisor);
            number /= divisor;
        }
        else
        {
            ++divisor;
        }

    }

    auto end = std::chrono::system_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    std::cout << "Elapsed time: " << duration.count() << std::endl;
    print_decompos(decompos);
    
    return 0;
}