class RandomInteger{
    private:
        int low;
        int high;
        int value;
    public:
        RandomInteger();
        RandomInteger(int low, int high);
        ~RandomInteger();

        void print() const;
};